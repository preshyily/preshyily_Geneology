#PRESHYPILY@GMAIL.COM
import os
from datetime import datetime
from pathlib import Path


# TASK: Logging System
# GLOBAL VARIABLES --------------------------------------------------------------------------------------------
PRESHGEN_AUTO_LOG = os.path.isfile(os.path.join(Path(__file__).resolve().parent.parent, 'preshgen_Logger.log'))
PRESHGEN_LOG_LAST_LINE = ''
NUM_REPS = 1
LOG_LEVEL = 2
now = datetime.now()
DT_STRING = now.strftime("%d/%m/%Y %H:%M:%S")
main_dir = Path(__file__).resolve().parent.parent

def presh_log(string, level=2):
    global PRESHGEN_AUTO_LOG
    global PRESHGEN_LOG_LAST_LINE
    global NUM_REPS
    string = str(string)
    file_dir = Path(__file__).resolve().parent.parent
    file_name = 'preshgen_Logger.log'
    file_path = os.path.join(file_dir, file_name)

    if not PRESHGEN_AUTO_LOG:
        try:
            with open(file_path, 'w') as file:
                file.write(f'[Logger created at {DT_STRING}]\n')
            PRESHGEN_AUTO_LOG = True
            presh_log(string)  # call presh_log function again to make sure actions are logged after file creation.
        except Exception as e:
            print(f'Error creating log file: {str(e)}')

    if PRESHGEN_AUTO_LOG and level <= LOG_LEVEL:
        try:
            if string == PRESHGEN_LOG_LAST_LINE:
                NUM_REPS += 1
            else:
                with open(file_path, 'a') as file:
                    if NUM_REPS > 1:
                        file.write(f'    (repeated {NUM_REPS} times)\n')
                    file.write(string + '\n')
                    PRESHGEN_LOG_LAST_LINE = string
                    NUM_REPS = 1
        except Exception as e:
            print(f'Error writing to log file: {str(e)}')
