from datetime import datetime

from util import readState, writeState
from constants import STATE_FILE


def do_nothing():
    pass


def start_working():
    now = datetime.now()
    timestamp = now.timestamp()
    writeState(STATE_FILE, 1, timestamp)


def add_one_minute():
    data = readState(STATE_FILE)
    stage = data.get('stage', 0)
    timestamp = data.get('timestamp', 0)
    timestamp += 60
    writeState(STATE_FILE, stage, timestamp)
    

def stop():
    now = datetime.now()
    timestamp = now.timestamp()
    writeState(STATE_FILE, 0, timestamp)