import json


def getServerip():
    return json.load(open('./config.json', 'r'))['ServerIp']
