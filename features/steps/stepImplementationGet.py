import requests
from behave import *

from utilities import resources
from utilities.resources import *


@given('I have the authentication token for get service')
def step_impl(context):
    context.authenticationToken = resources.Token


@when('I hit the get service to retrive the users list')
def step_impl(context):
    context.response = requests.get(resources.getEndpoint(), headers=resources.getHeaders())


@then('verify the status code of response is {statuscode:d} for get request')
def step_impl(context, statuscode):
    assert context.response.status_code == statuscode


@then('I retrive the user Id for any user')
def step_impl(context):
    responsedata = context.response.json()
    userIddetails= responsedata[0]['id']
    print(userIddetails)


@when('I hit the get service with specific user id details')
def step_impl(context):
    userId='6965857'
    endpoint = resources.getEndpoint() + "/" + userId
    print(endpoint)
    context.response = requests.get(endpoint, headers=resources.getHeaders())

@then('I validate the response details')
def step_impl(context):
    data = context.response.json()
    print(data['id'])
    print(data['name'])