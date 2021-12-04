
Feature: Cars_search test

Background:
    Given The PHPTravels main page is open

  Scenario Outline: Find a car using valid data
    Given Tab cars is open
    When Enter departure city "<city>"
    And Enter arrival city "<city2>"
    And Choose departure date "<date>"
    And Choose last date "<date2>"
    And Choose amount of adults "<adults>"
    And Search button is clicked
    Then Page with cars will open
    Examples:
      | city | city2      | date | date2 | adults |
      | Debrecen| Budapest | 24 | 27 | 4 |
      | Miskolc | Moscow  | 10   | 16  | 2  |
      | Moscow  |  Budapest |  2  | 5  | 1  |
      | Degerfors         | Stavropol         |  6  |  19 | 6  |