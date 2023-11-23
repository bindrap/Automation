Feature: Reporting Feature

  Scenario Outline: User generates a report
    Given the user is on the login page
    When the user logs in with username "Pbindra@citywindsor.ca"
    And navigates to the Reporting page
    And selects the required options on the Reporting page
    And generates the report
    Then the report should be downloaded successfully
    And the downloaded report should be moved to the destination folder
    


