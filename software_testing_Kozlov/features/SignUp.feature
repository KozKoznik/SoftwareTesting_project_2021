
Feature: Sign up page test

Background:
    Given The PHPTravels sign up page is open

  Scenario Outline: Create a new User using valid data
    Given Sign up page is open
    When Enter email "<email>"
    And The user has a first name of "<name>"
    And The user has a last name of "<surname>"
    And Phone is "<phone>"
    And Password of "<password>"
    And Signup button is clicked
    Then The account creation is successful
    Examples:
      | email                         | name    | surname     | password  |   phone      |
      | kozlov_example@email.com      | Nikita  | Kozlov      | 12345678  |  79624741387 |
      | kozlov_example2@mail.ru       | Ryan    | Gosling     | 38275293  |  79624745377 |
      | kozlov_example@yandex.ru      | Peter   | Jackson     | 12984000  |  79624741367 |
      | kozlov_example@ya.ru          | John    | Smith       | 98791054  |  79624742357 |



  Scenario: Unsuccessful registration - user already exists
    Given Sign up page is open
    When Enter email "kozlov_example@yandex.ru"
    And The user has a first name of "Nikita"
    And The user has a last name of "Kozlov"
    And Phone is "79624741387"
    And Password of "12345678"
    And Signup button is clicked
    Then The user gets the message that user already exist
