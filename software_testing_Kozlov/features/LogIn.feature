
Feature: Login test

Background:
    Given The PHPTravels login page is open

  Scenario Outline: Log in using not valid data
    Given Enter login "<email>" and password "<password>"
    When Login button is clicked
    Then Text error is shown
    Examples:
      | email                         | password | msg
      | kozlov_example@email.com      |           | Please fill out this field.|
      | kozlov_example2mail.ru        | 38275293  | Please include an '@' in the email address. 'koslov_example2mail.ru' is missing an '@' |
      |                               | 12984000  | Please fill out this field.|
      | Кириллица@yandex.ru           | 98791054  | A part followed by '@' should not contain the symbol 'К'.|


  Scenario: Log in using incorrect data
    Given Enter login "completelyrandomemail@email.com" and password "12JKJiis"
    When Login button is clicked
    Then User gets the message Wrong credentials


  Scenario: Log in using correct data
    Given Enter login "kozlov_example@yandex.ru" and password "12984000"
    When Login button is clicked
    Then Login is successful

