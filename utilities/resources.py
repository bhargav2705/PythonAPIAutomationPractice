import random
import string

from utilities.config import getConfig


class resources:
    Token = "ff3084332f0f685c0cfbfaf4e132ff0265dea575a09bb2ea5ee305873c0c8dd0"

    def __init__(self):
        print("Constructor")

    @classmethod
    def PostEndpoint(self):
        postEndpoint = getConfig()['API']['url'] + getConfig()['API']['postEndpoint']
        return postEndpoint

    @classmethod
    def getEndpoint(self):
        getEndpoint = getConfig()['API']['url'] + getConfig()['API']['getEndpoint']
        return getEndpoint

    @classmethod
    def getHeaders(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + resources.Token
        }
        return headers

    @classmethod
    def generateRuntimeEmail(self):
       letters = string.ascii_letters
       random_string = ''.join(random.choice(letters) for i in range(6)) + "@gmail.com"
       return random_string




