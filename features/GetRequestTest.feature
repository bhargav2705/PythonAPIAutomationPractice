Feature: Get Request-for Go Rest-API Automation

  Scenario: Verify the Get Request for Sample Go Rest API 1
    Given I have the authentication token for get service
    When I hit the get service to retrive the users list
    Then verify the status code of response is 200 for get request
    And I retrive the user Id for any user

  Scenario: Verify the Get  request for Sample Go Rest API 2
    Given  I have the authentication token for get service
    When I hit the get service with specific user id details
    Then verify the status code of response is 200 for get request
    And I validate the response details



