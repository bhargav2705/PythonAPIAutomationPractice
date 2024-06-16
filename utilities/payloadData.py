import json


def createPayload():
    f = open('utilities/PostRequestPayload.json')
    payload = json.load(f)
    return payload
