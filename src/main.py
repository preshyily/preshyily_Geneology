#PRESHYPILY@GMAIL.COM

from sims.sim_info_manager import SimInfoManager
from date_and_time import DateAndTime
from time_service import TimeService
from helpers.injector import inject
from presh_logging import presh_log, PRESHGEN_AUTO_LOG
from presh_sim import PreshSim
from datetime import datetime
from pathlib import Path
import os
import sys
import json
import services
import configparser

#TASK: SAVE-SPECIFIC TRACKING

# GLOBAL VARIABLES --------------------------------------------------------------------------------------------
AUTO_UPDATE_JSON = False
CONSANG_LIMIT = 2 ** -5
CURR_SESSION_ENABLED = False
DISABLE_NOTIFS = False
DREL_INCEST = True
FILE_NAME_EXTRA = 'PRESH_DEFAULT'
IREL_INCEST = True
MCCC_AUTOSAVE_ENABLED = False
MCCC_AUTOSAVE_HEXSLOTNUMBER = ''
MCCC_AUTOSAVE_MAXSAVENUMBER = 0
MCCC_AUTOSAVES = []
OVERALL_SIM_DAYS = 0
PRESHGEN_AUTO_ENABLED = False
SAVE_SLOT_ID = '00000000'
SHOW_CONSANG = False
# datetime object containing current date and time
now = datetime.now()
DT_STRING = now.strftime("%d/%m/%Y %H:%M:%S")


config_key_list = [
    'advanced_use_currentsession_files',
    'auto_update_json',
    'consanguinity_limit',
    'disable_notifs',
    'direct_rels_are_incestuous',
    'file_name_extra',
    'indirect_rels_are_incestuous',
    'mccc_autosave_enabled',
    'mccc_autosaves',
    'overall_sim_days',
    'preshgen_auto_enabled',
    'save_slot_id',
    'show_consanguinity_in_notifs'
]

preset_modifiers = [
    str(CURR_SESSION_ENABLED),
    str(AUTO_UPDATE_JSON),
    str(CONSANG_LIMIT),
    str(DISABLE_NOTIFS),
    str(DREL_INCEST),
    str(FILE_NAME_EXTRA),
    str(IREL_INCEST),
    str(MCCC_AUTOSAVE_ENABLED),
    str(MCCC_AUTOSAVES),
    str(OVERALL_SIM_DAYS),
    str(PRESHGEN_AUTO_ENABLED),
    SAVE_SLOT_ID,
    str(SHOW_CONSANG)
]

#TASK: Environment Setup
main_dir = Path(__file__).resolve().parent.parent
config = configparser.ConfigParser()
main_header = 'PreshGen Settings'

# GLOBAL VARIBALES END ----------------------------------------------------------------------------------------

# CONFIGURATION MANAGEMENT
# CONFIG HELPERS --------------------------------------------------------------------------------------------------

def get_config_dir():
    log_name = "preshgen_Settings.cfg"
    config_dir = os.path.join(main_dir, log_name)
    return config_dir

def config_prep_file():
    with open(get_config_dir(), "w") as config_file:
        config_file.write(f"[{main_header}]")
        for incrementor in range(len(config_key_list)):
            config_file.write(f"\n{config_key_list[incrementor]} = {preset_modifiers[incrementor]}")
        config_file.close()

def config_init_check():
    with open(get_config_dir(), "r") as config_file:
        config.read_file(config_file)
        for incrementor in range(len(config_key_list)):
            if not config.has_option(main_header, config_key_list[incrementor]):
                append_option(incrementor)

def update_config(setting, value):
    try:
        if not config.has_section(main_header):
            config.add_section(main_header)
        config.set(main_header, setting, str(value))
        with open(get_config_dir(), 'w') as config_file:
            config.write(config_file)
        presh_log(f"Updated config setting {setting} to {value}")
    except Exception as e:
        presh_log(f"Error updating config setting {setting}: {e}")

def append_option(index):
    with open(get_config_dir(), "a") as config_file:
        config_file.write(f"\n{config_key_list[index]} = {preset_modifiers[index]}")
        config_file.close()

def option_toggle(identifier):
    option = config_key_list[identifier]
    if not config.has_option(main_header, option):
        append_option(identifier)
    else:
        with open(get_config_dir(), "r") as config_file:
            config.read_file(config_file)
            setting_value = config.getboolean(main_header, option)
            value = "False" if setting_value else "True"
            config.set(main_header, option, value)
            with open(get_config_dir(), "w") as config_file_write:
                config.write(config_file_write)

def get_slot():
    per = services.get_persistence_service()
    int_slot_id = int(per._save_game_data_proto.save_slot.slot_id)
    hex_slot_id_tmp = hex(int_slot_id)[2:]
    hex_slot_id = ('0' * (8 - len(hex_slot_id_tmp))) + hex_slot_id_tmp
    return hex_slot_id

def format_sim_date(return_type='fullstring'):
    simNow = str(services.time_service().sim_now)
    listNow = simNow.split(' ')
    simWeek = listNow[2].split(':')
    simDay = listNow[1].split(':')
    simTime = listNow[0].split('.')
    if 0 <= int(simDay[1]):
        simWeekNumber = 1 + int(simWeek[1])
        simDayNumber = 1 + int(simDay[1])
        if return_type == 'fullstring':
            simTimeNow = f'week {simWeekNumber} day {simDayNumber} {simTime[0]}'
            return simTimeNow
        elif return_type == 'day':
            return simDayNumber
        elif return_type == 'week':
            return simWeekNumber

# CONFIG HELPERS END ------------------------------------------------------------------------------------------

# LOGGER-CONFIG INIT -------------------------------------------------------------------------------------------------
# Mod Initialization
def start_logging():
    global MCCC_AUTOSAVE_ENABLED
    global MCCC_AUTOSAVE_HEXSLOTNUMBER
    global MCCC_AUTOSAVE_MAXSAVENUMBER
    global PRESHGEN_AUTO_LOG
    global SAVE_SLOT_ID
    global OVERALL_SIM_DAYS

    if not PRESHGEN_AUTO_LOG:
        presh_log(f'[started logging at {DT_STRING}]', 1)
        presh_log('', 1)

    mods_path = Path(__file__).resolve()
    appendage = '/'
    while not os.path.basename(mods_path) == 'Mods':
        mods_path = mods_path.parent
        appendage = '.' + appendage
    sys.path.append(appendage)

    try:
        mccc_cfg_path = None
        for root, dirs, files in os.walk(mods_path):
            for name in files:
                if name.startswith('mc_settings') and name.endswith('cfg'):
                    mccc_cfg_path = root + os.sep + name
                    break
        if mccc_cfg_path is not None:
            with open(mccc_cfg_path, 'r') as mccc_cfg:
                mccc_cfg_dict = json.load(mccc_cfg)
                presh_log('FOUND mc_settings.cfg', 1)
        else:
            presh_log('did NOT find mc_settings.cfg', 1)
        if mccc_cfg_path:
            MCCC_AUTOSAVE_ENABLED = mccc_cfg_dict['Autosave_Enabled']
            MCCC_AUTOSAVE_HEXSLOTNUMBER = mccc_cfg_dict['Autosave_HexSlotNumber']
            MCCC_AUTOSAVE_MAXSAVENUMBER = mccc_cfg_dict['Autosave_MaxSaveNumber']
        else:
            MCCC_AUTOSAVE_ENABLED = False
            MCCC_AUTOSAVE_HEXSLOTNUMBER = ''
            MCCC_AUTOSAVE_MAXSAVENUMBER = 0
    except Exception as ex:
        presh_log(f'mc_settings not grabbed from .cfg: {ex}', 1)
        MCCC_AUTOSAVE_ENABLED = False
        MCCC_AUTOSAVE_HEXSLOTNUMBER = ''
        MCCC_AUTOSAVE_MAXSAVENUMBER = 0

    if MCCC_AUTOSAVE_ENABLED:
        smallest_save = int('0x' + str(MCCC_AUTOSAVE_HEXSLOTNUMBER), 16)
        for i in range(MCCC_AUTOSAVE_MAXSAVENUMBER):
            int_slot_id = smallest_save + i
            hex_slot_id_tmp = hex(int_slot_id)[2:]
            hex_slot_id = ('0' * (8 - len(hex_slot_id_tmp))) + hex_slot_id_tmp
            MCCC_AUTOSAVES.append(hex_slot_id)
        presh_log(f'autosave slots = {MCCC_AUTOSAVES}')
    #write and save config file
    try:
        if not os.path.exists(get_config_dir()):
            config_prep_file()
        config_init_check()

        config.set(main_header, 'save_slot_id', SAVE_SLOT_ID)
        config.set(main_header, 'overall_sim_days', str(OVERALL_SIM_DAYS)) 

        # TODO: set config here for irel, drel, cos ang, sims, etc.

        with open(get_config_dir(), 'w') as config_file:
            config.write(config_file)
            presh_log('Updated main mod section in preshgen_Settings')

    except Exception as e:
        presh_log(f'error updating config file: {str(e)}')

# LOGGER-CONFIG INIT END ---------------------------------------------------------------------------------------

# GET-SAVE-LOG GAME DATA --------------------------------------------------------------------------------------------------

# Initialization function to create PreshSim objects for each Sim (SimInfo Object) in the Save
def init_presh_sims():
    presh_sim_objects = []
    try:
        for sim_info in services.sim_info_manager().get_all():
            try:
                presh_sim = PreshSim(sim_info)
                presh_sim_objects.append(presh_sim)
            except Exception as e:
                presh_log(f'Error initializing PreshSim for sim_id {sim_info.sim_id}: {e}')
    except Exception as e:
        presh_log(f'Error initializing PreshSim objects: {e}')
    return presh_sim_objects

#Begin only after save has completed loading.
@inject(SimInfoManager, 'on_all_households_and_sim_infos_loaded')
def on_all_households_and_sim_infos_loaded(original, self, *args, **kwargs):
    result = original(self, *args, **kwargs)
    global SAVE_SLOT_ID
    global OVERALL_SIM_DAYS

    SAVE_SLOT_ID = get_slot()
    OVERALL_SIM_DAYS = format_sim_date('day')
    start_logging()
    
    PreshSims = init_presh_sims()
    presh_log(f'Initialized {len(PreshSims)} PreshSim objects in Save: {SAVE_SLOT_ID}')
    
    #Testing
    random_sim = random.choice(PreshSims)
    presh_log(f'Random PreshSim Object: {random_sim} {random_sim.age_in_days} {random_sim.home_region} {random_sim.birth_location} ')
    
    return result


