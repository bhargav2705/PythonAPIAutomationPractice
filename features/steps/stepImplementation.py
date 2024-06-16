import requests
from behave import *
from utilities.payload.AddPayload import *
from utilities.resources import *


headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + resources.Token
}


@given('I have the authentication token')
def step_impl(context):
    context.authenticationToken = resources.Token


@then('I create the payload')
def step_impl(context):
    context.payload = AddPayload.createPayload(resources.generateRuntimeEmail())


@when('I hit the post endpoint for Go Rest')
def step_impl(context):
    context.response = requests.post(resources.PostEndpoint(), json=context.payload, headers=headers)
    # print(resources.getHeaders())
    print(context.response.json())


@then('verify the status code of response is {statusCode:d}')
def step_impl(context,statusCode):
    assert context.response.status_code == statusCode


@then('retrieve the Id from response')
def step_impl(context):
    responseData = context.response.json()
    print(responseData['id'])
