import json


class AddPayload:
    def createPayload(emailId):
        f = 'utilities/PostRequestPayload.json'
        with open(f) as file:
            data = json.load(file)
            data['email'] = emailId
        print(data)
        return data
