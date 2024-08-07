#PRESHYPILY@GMAIL.COM
from sims.sim_info_manager import SimInfoManager
from sims.sim_info_types import Gender
from sims.sim_info import SimInfo
from presh_logging import presh_log
import services


class PreshSim:
    #TASK: Initialization of Sim Objects
    def __init__(self, sim_info):
        if isinstance(sim_info, SimInfo):
            self.sim_id = sim_info.sim_id
            self.first_name = sim_info.first_name
            self.last_name = sim_info.last_name
            self.is_female = sim_info.gender == Gender.FEMALE
            self.time = services.time_service().sim_now.absolute_ticks()
            self.age_in_days = sim_info.age
            self.home_region = sim_info.zone_id
            self.is_culled = False

            #testing output of sim_info.get_home_lot()
            self.birth_location = sim_info.get_home_lot()
            
            self.direct_relationships = []
            self.friendship_relationships = []
            self.in_law_relationships = []
            self.indirect_relationships = []
            self.romantic_relationships = []
            self.special_relationships = []
            self.step_relationships = []

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
                self.age_in_days = sim_info.age
                change = True

            if self.home_region != sim_info.zone_id:
                presh_log(f'updated sim home_region: {self.home_region} to --> {sim_info.zone_id}')
                self.home_region = sim_info.zone_id
                change = True
           
            if change:
                self.time = services.time_service().sim_now.absolute_ticks()
                presh_log(f'completed preshsim info update at {self.time}')
            
            #birth_location will only need to be initalized once and never updated.
    

    def to_dict(self):
        return {
            'sim_id': self.sim_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_female': self.is_female,
            'time': self.time,
            'age_in_days': self.age_in_days,
            'home_region': self.home_region,
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