import json

from datetime import datetime

def writeState(file_name, stage, timestamp):
    data = {
        'stage': stage,
        'timestamp': timestamp
    }

    with open(file_name, "w") as file_:
        json.dump(data, file_)


def readState(file_name):
    try:
        with open(file_name, "r") as file_:
            try:
                return json.load(file_)
            except json.decoder.JSONDecodeError:
                return {}
    except FileNotFoundError:
        now = datetime.now()
        timestamp = now.timestamp()
        writeState(file_name, 0, timestamp)
        return readState(file_name)