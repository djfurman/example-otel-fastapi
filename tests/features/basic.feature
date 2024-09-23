Feature: Basic API functionality

    Scenario: Run a healthcheck
    Given we are running an API
    When we GET the "/health" endpoint
    Then we should receive a 200 response
    And the response should contain "isHealthy"
    And the response key "isHealthy" should be True
