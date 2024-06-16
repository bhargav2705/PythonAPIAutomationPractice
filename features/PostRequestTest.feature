Feature: Post Request-for Go Rest-API Automation

  Scenario: Verify the Post request for Sample Go Rest API
    Given I have the authentication token
    Then I create the payload
    When I hit the post endpoint for Go Rest
    Then verify the status code of response is 201
    And  retrieve the Id from response
