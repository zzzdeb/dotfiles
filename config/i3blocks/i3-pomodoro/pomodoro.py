import os

from datetime import datetime, timedelta
from subprocess import call

from constants import STATE_FILE, ENABLE_NOTIFICATIONS
from stages import STAGES
from util import readState, writeState


def print_time(label, remaining_time):
    if remaining_time.seconds > 59:
        minutes = int(remaining_time.seconds / 60)
        print(f'{label} {minutes}min')
    else:
        print(f'{label} {remaining_time.seconds}s')


if __name__ == "__main__":
    data = readState(STATE_FILE)
    stage = data.get('stage', 0)
    timestamp = data.get('timestamp', 0)
    stage_obj = STAGES[stage]

    if os.environ.get('BLOCK_BUTTON') == "1":
        stage_obj.left_click()
    elif os.environ.get('BLOCK_BUTTON') == "3":
        stage_obj.right_click()

    now = datetime.now()
    diff = int(now.timestamp() - float(timestamp))

    remaining_time = timedelta(seconds=stage_obj.minutes * 60 - diff)
    if (remaining_time.total_seconds() <= 0
        and stage_obj.minutes != -1):
            now = datetime.now()
            timestamp = now.timestamp()
            writeState(STATE_FILE, stage_obj.next_stage.index, timestamp)

            if stage_obj.notification != '' and ENABLE_NOTIFICATIONS:
                try:
                    call(['notify-send', 'Pomodoro', stage_obj.notification, '-t', '5000'])
                except FileNotFoundError:
                    print("`notify-send` wasn't recognized.")
 
    stage_obj.print_(stage_obj.label, remaining_time)