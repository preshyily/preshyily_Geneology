#PRESHYPILY@GMAIL.COM
from functools import lru_cache
from sims4.resources import Types
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
                self.sim_id = data['sim_id']
                self.first_name = data['first_name']
                self.last_name = data['last_name']
                self.is_female = data['is_female']
                self.time = data['time']
                self.age_in_days = data['age_in_days']
                self.home_region = data['home_region']
                self.is_culled = data['is_culled']
                self.birth_location = data['birth_location']
                self.direct_relationships = data['direct_relationships']
                self.friendship_relationships = data['friendship_relationships']
                self.in_law_relationships = data['in_law_relationships']
                self.indirect_relationships = data['indirect_relationships']
                self.romantic_relationships = data['romantic_relationships']
                self.special_relationships = data['special_relationships']
                self.step_relationships = data['step_relationships']

    def calculate_age_in_days(self, sim_info):
        #Zembee P4_Sims4Lib.py
        age_transition_data = sim_info.get_age_transition_data(sim_info.age)
        currentagespan = age_transition_data.get_age_duration(sim_info)
        days_in_age = sim_info.days_until_ready_to_age()
        if sim_info.is_elder:
            agebonus = sim_info._get_bonus_days()
        else:
            agebonus = 0.0
        days_in_age = days_in_age + agebonus
        return days_in_age
    
    def get_current_zone_name(self, sim_info):
        #Zembee P4_Sims4Lib.py
        zone_name = "unknown"
        persistence_service = services.get_persistence_service()
        zone_data = persistence_service.get_zone_proto_buff(sim_info.household.home_zone_id)
        if zone_data is not None:
            zone_name = zone_data.name
        return zone_name

    def get_current_world_name(self, sim_info):
        #Zembee P4_Sims4Lib.py
        world_name = "unknown"
        persistence_service = services.get_persistence_service()
        world_data = persistence_service.get_neighborhood_proto_buf_from_zone_id(sim_info.zone_id)
        if world_data is not None:
            world_name = world_data.name
        return world_name

    def update_all_sim_info(self, sim_info):
        if isinstance(sim_info, SimInfo):
            change = False
            if self.sim_id != sim_info.sim_id:
                presh_log(f'updated sim_id: {self.sim_id} to --> {sim_info.sim_id}')
                self.sim_id = sim_info.sim_id
                change = True

            if self.first_name != sim_info.first_name:
                presh_log(f'updated sim first_name: {self.first_name} to --> {sim_info.first_name}')
                self.first_name = sim_info.first_name
                change = True

            if self.last_name != sim_info.last_name:
                presh_log(f'updated sim last_name: {self.last_name} to --> {sim_info.last_name}')
                self.last_name = sim_info.last_name
                change = True

            if self.is_female != (sim_info.gender == Gender.FEMALE):
                presh_log(f'updated sim gender: {self.is_female} to --> {sim_info.gender == Gender.FEMALE}')
                self.sim_id = sim_info.gender == Gender.FEMALE
                change = True

            if self.age_in_days != sim_info.age:
                presh_log(f'updated sim age: {self.age_in_days} to --> {sim_info.age}')
                self.age_in_days = self.calculate_age_in_days(sim_info)
                change = True

            if self.home_region != sim_info.zone_id:
                presh_log(f'updated sim home_region: {self.home_region} to --> {sim_info.zone_id}')
                self.home_region = sim_info.zone_id
                change = True
           
            if change:
                self.time = services.time_service().sim_now.absolute_ticks()
                presh_log(f'completed preshsim info update at {self.time}')
            
            #birth_location will only need to be initalized once and never updated.
#TASK: INIT OF SIM OBJS TO PRESHSIM OBJS END ---------------------------------------------------------------

# TASK: RELATIONSHIP TRACKING ------------------------------------------------------------------------------
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

    def determine_relationship_name(self, generational_difference):
        if generational_difference == 1:
            return "parent"
        elif generational_difference == 2:
            return "grandparent"
        elif generational_difference > 2:
            return f"great{'-great' * (generational_difference - 3)} grandparent"
        elif generational_difference == -1:
            return "child"
        elif generational_difference == -2:
            return "grandchild"
        elif generational_difference < -2:
            return f"great{'-great' * (abs(generational_difference) - 3)} grandchild"
        else:
            return None

    def remove_duplicate_relationships(self, relationships):
        seen = set()
        unique_relationships = []
        for rel in relationships:
            rel_tuple = (rel['relation'], rel['sim_id'])
            if rel_tuple not in seen:
                seen.add(rel_tuple)
                unique_relationships.append(rel)
        return unique_relationships

    def get_direct_relationships(self, sim_info):
        manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
        direct_relationships = []

        relationship_bits = {
            'grandparent': 0x2268,
            'parent': 0x2269,
            'child': 0x2265,
            'grandchild': 0x2267,
        }

        for other_sim_info in services.sim_info_manager().get_all():
            for rel_name, bit_id in relationship_bits.items():
                rel_bit = manager.get(bit_id)
                if sim_info.relationship_tracker.has_bit(other_sim_info.sim_id, rel_bit):
                    direct_relationships.append({'relation': rel_name, 'sim_id': other_sim_info.sim_id})
                    break 

            if not relationship_name:
                gen_diff = self.calculate_generational_difference(sim_info, other_sim_info)
                if gen_diff == 0:
                    continue
                relationship_name = self.determine_relationship_name(gen_diff)

            direct_relationships.append({
                'relation': relationship_name, 
                'sim_id': other_sim_info.sim_id
            })

        # Add children to direct relationships
        for child in self.get_children(sim_info):
            direct_relationships.append({
                'relation': 'child',
                'sim_id': child.sim_id
            })

        # Remove duplicates
        return self.remove_duplicate_relationships(direct_relationships)

        def calculate_consanguinity(self, sim_x, sim_y):
            direct_rel_percentage = self.drel_percent(sim_x.sim_id, sim_y.sim_id)
            indirect_rel_percentage = self.irel_percent(sim_x.sim_id, sim_y.sim_id)
            total_consanguinity = direct_rel_percentage + indirect_rel_percentage

            return total_consanguinity

        @lru_cache(maxsize=None)
        def drel_percent(self, x_id, y_id):
            if int(y_id) < int(x_id):
                return self.drel_percent(y_id, x_id)

            generations = self.calculate_generational_difference(self.get_rivsim_from_id(x_id), self.get_rivsim_from_id(y_id))
            if generations > 0:
                return 0.5 ** generations
            return 0

        @lru_cache(maxsize=None)
        def irel_percent(self, x_id, y_id):
            if int(y_id) < int(x_id):
                return self.irel_percent(y_id, x_id)

            irel = self.get_indirect_relation(self.get_rivsim_from_id(x_id), self.get_rivsim_from_id(y_id))
            irel_percentage = sum(0.5 ** (rel[2] + rel[3]) for rel in irel)

            return irel_percentage if irel_percentage >= CONSANG_LIMIT else 0

# TASK: RELATIONSHIP TRACKING END----------------------------------------------------------------------------

    def to_dict(self):
        return {
            'sim_id': self.sim_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_female': self.is_female,
            'time': self.time,
            'age_in_days': self.age_in_days,
            'home_region': self.home_region,
            'is_culled': self.is_culled,
            'birth_location': self.birth_location,
            'direct_relationships': self.direct_relationships,
            'friendship_relationships': self.friendship_relationships,
            'in_law_relationships': self.in_law_relationships,
            'indirect_relationships': self.indirect_relationships,
            'romantic_relationships': self.romantic_relationships,
            'special_relationships': self.special_relationships,
            'step_relationships': self.step_relationships
        }

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
        return f"<PreshSim {self.sim_id} {self.first_name} {self.last_name}>"
