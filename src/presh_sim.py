#PRESHYPILY@GMAIL.COM
from functools import lru_cache
from sims4.resources import Types
from sims.genealogy_tracker import GenealogyTracker, FamilyRelationshipIndex
from sims.sim_info_manager import SimInfoManager
from sims.sim_info_types import Age, Gender
from traits.traits import TraitType
from sims.sim_info import SimInfo
from presh_logging import presh_log
import services

CONSANG_LIMIT = 2 ** -5
class PreshSim:
#TASK: INIT OF SIM OBJS TO PRESHSIM OBJS -------------------------------------------------------------------
    def __init__(self, sim_info=None, data=None):
        if sim_info:
            self.sim_id = sim_info.sim_id
            self.first_name = sim_info.first_name
            self.last_name = sim_info.last_name
            self.is_female = sim_info.gender == Gender.FEMALE
            self.time = services.time_service().sim_now.absolute_ticks()
            self.age_in_days = self.calculate_age_in_days(sim_info)
            self.home_region = sim_info.zone_id
            self.is_culled = False
            self.birth_location = self.get_current_zone_name(sim_info)
            self.direct_relationships = []
            self.friendship_relationships = []
            self.in_law_relationships = []
            self.indirect_relationships = []
            self.romantic_relationships = []
            self.special_relationships = []
            self.step_relationships = []
        elif data:
            self.__dict__.update(data)

    def calculate_age_in_days(self, sim_info):
        age_transition_data = sim_info.get_age_transition_data(sim_info.age)
        days_in_age = sim_info.days_until_ready_to_age() + (sim_info._get_bonus_days() if sim_info.is_elder else 0.0)
        return days_in_age

    def get_current_zone_name(self, sim_info):
        zone_data = services.get_persistence_service().get_zone_proto_buff(sim_info.household.home_zone_id)
        return zone_data.name if zone_data else "unknown"

    def get_current_world_name(self, sim_info):
        #Zembee P4_Sims4Lib.py
        world_name = "unknown"
        persistence_service = services.get_persistence_service()
        world_data = persistence_service.get_neighborhood_proto_buf_from_zone_id(sim_info.zone_id)
        if world_data is not None:
            world_name = world_data.name
        return world_name

    def update_all_sim_info(self, sim_info):
        changes = {}
        fields = ['sim_id', 'first_name', 'last_name', 'gender', 'age_in_days', 'zone_id']
        for field in fields:
            new_value = getattr(sim_info, field, None)
            if getattr(self, field) != new_value:
                changes[field] = new_value

        if changes:
            presh_log(f'Updated sim {self.sim_id} info: {changes}')
            self.__dict__.update(changes)
            self.time = services.time_service().sim_now.absolute_ticks()
            self.direct_relationships = self.get_direct_relationships(sim_info)
            self.indirect_relationships = self.get_indirect_relationships(sim_info)
            self.romantic_relationships = self.get_romantic_relationships(sim_info)
    
            #birth_location will only need to be initalized once and never updated.
#TASK: INIT OF SIM OBJS TO PRESHSIM OBJS END ---------------------------------------------------------------

# TASK: RELATIONSHIP TRACKING ------------------------------------------------------------------------------
    @lru_cache(maxsize=None)
    def get_relationships(self, sim_info, relationship_bits):
        manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
        relationships = []
        
        genealogy_tracker = sim_info.genealogy
        with genealogy_tracker.genealogy_caching():
            for other_sim_info in services.sim_info_manager().get_all():
                if sim_info == other_sim_info:
                    continue

                relationship_name = None
                for rel_name, bit_id in relationship_bits.items():
                    rel_bit = manager.get(bit_id)
                    if sim_info.relationship_tracker.has_bit(other_sim_info.sim_id, rel_bit):
                        relationship_name = rel_name
                        relationships.append((relationship_name, other_sim_info.sim_id))
                        break

                if not relationship_name:
                    if other_sim_info.sim_id in genealogy_tracker.get_parent_sim_ids_gen():
                        relationship_name = 'parent'
                    elif other_sim_info.sim_id in genealogy_tracker.get_children_sim_ids_gen():
                        relationship_name = 'child'
                    elif other_sim_info.sim_id in genealogy_tracker.get_grandparent_sim_ids_gen():
                        relationship_name = 'grandparent'
                    elif other_sim_info.sim_id in genealogy_tracker.get_siblings_sim_ids_gen():
                        relationship_name = 'sibling'

                    if relationship_name:
                        gen_diff = self.calculate_generational_difference(sim_info, other_sim_info)
                        relationship_name = self.determine_relationship_name(gen_diff, relationship_name)
                        relationships.append((relationship_name, other_sim_info.sim_id))

        return self.remove_duplicate_relationships(relationships)


    def get_children(self, sim_info):
        child_bit = services.get_instance_manager(Types.RELATIONSHIP_BIT).get(0x2265)
        return [other_sim_info for other_sim_info in services.sim_info_manager().get_all()
                if sim_info.relationship_tracker.has_bit(other_sim_info.sim_id, child_bit)]
    
    @lru_cache(maxsize=None)
    def calculate_generational_difference(self, sim_x, sim_y, current_gen=0):
        if sim_y in self.get_children(sim_x):
            return current_gen + 1

        for child in self.get_children(sim_x):
            gen_diff = self.calculate_generational_difference(child, sim_y, current_gen + 1)
            if gen_diff > 0:
                return gen_diff

        return 0

    def determine_relationship_name(self, generational_difference, relationship_type=None):
        #Direct Relationships
        if relationship_type in ['parent', 'child']:
                base_name = 'parent' if relationship_type == 'parent' else 'child'
                return self.format_generational_title(base_name, generational_difference)
        
        #Indirect Relationships
        elif relationship_type == 'sibling':
            return "sibling" if generational_difference == 0 else "distant sibling"

        elif relationship_type == 'cousin':
            cousin_level = abs(generational_difference) + 1
            return f"{cousin_level}th cousin" if generational_difference == 0 else f"{cousin_level}th cousin {abs(generational_difference)} times removed"

        elif relationship_type == 'pibling':
            return self.format_generational_title("aunt/uncle", generational_difference)

        elif relationship_type == 'nibling':
            return self.format_generational_title("niece/nephew", -generational_difference)

        #Romantic Relationships
        elif relationship_type in ['spouse', 'widow/widower', 'dead_spouse']:
            return "spouse"
        elif relationship_type == 'engaged' or relationship_type == 'promised':
            return "engaged/promised"
        elif relationship_type in ['partner', 'faithful', 'soulmates']:
            return "partner"
        elif relationship_type in ['romantic_interest', 'getting_married', 'lovebirds', 'lovers', 'sweethearts']:
            return "romantic partner"
        
        # Negative Romantic Relationships
        elif relationship_type in ['just_broke_up_or_divorced', 'broken_up', 'broken_up_engaged', 'divorced', 'despised_ex', 'frustrated_ex']:
            return "ex-partner"
        elif relationship_type in ['got_cold_feet', 'left_at_the_altar']:
            return "failed engagement"
        elif relationship_type in ['awkward_friends', 'awkward_lovers', 'bad_match', 'terrible_match', 'total_opposites', 'bad_romance']:
            return "unfortunate romance"
        elif relationship_type == 'enemies_with_benefits':
            return "enemies with benefits"
        elif relationship_type in ['has_been_unfaithful', 'cheated_with']:
            return "unfaithful partner"
        
        # Miscellaneous Romantic Relationships
        elif relationship_type in ['first_kiss', 'recent_first_kiss']:
            return "first kiss"
        elif relationship_type in ['have_done_woohoo', 'have_done_woohoo_recently']:
            return "WooHoo partner"
        elif relationship_type == 'exchanged_numbers':
            return "flirtatious acquaintance"
        elif relationship_type in ['its_awkward', 'its_complicated', 'its_very_awkward', 'its_very_complicated']:
            return "complicated relationship"
        elif relationship_type in ['frenemies', 'hot_and_cold']:
            return "unstable relationship"
        elif relationship_type in ['romantic_acquaintances', 'just_friends', 'just_good_friends']:
            return "casual acquaintance"
        elif relationship_type in ['romantic_disliked', 'romantic_despised']:
            return "disliked romantic partner"
        
        return "unknown"

    def get_direct_relationships(self, sim_info):
            relationship_bits = {
                'parent': 0x2269,
                'child': 0x2265,
                'grandparent': 0x2268,
                'grandchild': 0x2267,
            }
            return self.get_relationships(sim_info, relationship_bits)

    def get_indirect_relationships(self, sim_info):
        relationship_bits = {
            'sibling': 0x2262,
            'cousin': 0x227A,
            'pibling': 0x227D,   # Aunt/Uncle
            'nibling': 0x2705    # Nephew/Niece
        }
        return self.get_relationships(sim_info, relationship_bits)

    def get_romantic_relationships(self, sim_info):
        romantic_bits = {
            'spouse': 0x3DCE,
            'engaged': 0x3DC8,
            'romantic_interest': 0x3DDE,
            'lover': 0x3DDD,
        }
        return self.get_relationships(sim_info, romantic_bits)

    def remove_duplicate_relationships(self, relationships):
        seen = set()
        return [rel for rel in relationships if rel not in seen and not seen.add(rel)]

    def get_in_law_relationships(self, sim_info): 
        spouse_relationships = []
        try:
            for relationship in self.romantic_relationships:
                if relationship['relation'] == 'spouse':
                    spouse_info = services.sim_info_manager().get(relationship['sim_id'])
                    if spouse_info:
                        # Fetch direct relationships of the spouse
                        spouse_direct_rels = self.get_direct_relationships(spouse_info)
                        spouse_indirect_rels = self.get_indirect_relationships(spouse_info)

                        # Check if the direct relationships are empty and log an error if they are
                        if not spouse_direct_rels:
                            presh_log(f'Error: Direct relationships are empty for sim_id: {spouse_info.sim_id}')
                        
                        # Add in-law relationships based on the spouse's family members
                        for rel in spouse_direct_rels + spouse_indirect_rels:
                            # Avoid extending beyond immediate family
                            if rel['relation'] in ['parent', 'sibling', 'grandparent']:
                                spouse_relationships.append({
                                    'relation': f"{rel['relation']} in-law",
                                    'sim_id': rel['sim_id']
                                })

            # Remove duplicates
            self.in_law_relationships = self.remove_duplicate_relationships(spouse_relationships)

        except Exception as e:
            presh_log(f'Error in get_in_law_relationships for sim_id {sim_info.sim_id}: {e}')


# TASK: RELATIONSHIP TRACKING END----------------------------------------------------------------------------
    def to_dict(self):
        return self.__dict__.copy()

    def cull(self):
        if not self.is_culled:
            self.is_culled = True
            # TODO: remove marriages if necessary
            # Example: self.marriages = []
    
    def uncull(self):
        if self.is_culled:
            self.is_culled = False
    
    def __repr__(self):
        return f"<PreshSim {self.sim_id} {self.first_name} {self.last_name}>"
        
    def __str__(self):
        return self.__repr__()