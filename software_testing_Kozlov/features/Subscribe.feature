
Feature: Subscribe test

Background:
    Given The PHPTravels page is open

    Scenario Outline: Subscribe with non-valid email
    Given Subscribe field is visible
    When Enter "<email>"
    And Subscribe button is clicked
    Then Get error message "<msg>"
    Examples:
      | email                     | msg |
      |   NULL                    | Please add email!   |
      | @yandex.ru                | Please add correct email!    |
      | 1234567890                | Please add correct email!    |
      | kozlovnikitos             | Please add correct email!    |

    Scenario: Subscribe with valid email
    Given Subscribe field is visible
    When Enter "kozkoznik@yandex.ru"
    And Subscribe button is clicked
    Then Get approval message "Thank you for subscription"

