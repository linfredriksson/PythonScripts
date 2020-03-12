import json
import os


def readJson(path):
    data = None
    if not os.path.exists(path):
        return data
    with open(path, "r") as in_file:
        data = json.load(in_file)
    return data


def writeJson(path, data):
    try:
        with open(path, "w") as out_file:
            json.dump(data, out_file)
        return True
    except:
        return False
