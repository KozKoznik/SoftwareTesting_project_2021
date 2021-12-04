
Feature: Contact us page test

Background:
    Given The PHPTravels is open

  Scenario Outline: Contact us with invalid data
    Given Contact us page is open
    When Enter contact "<email>"
    And Enter your name "<name>"
    And Enter feedback "<message>"
    And Resolve captcha
    And Click Send button
    Then Get error message
    Examples:
      | name      | email              |  message                |
      |  Nikita   | Lalala@            | Lorem ipsum bla-bla-bla |
      |  NULL     | 123sa              | NULL                    |
      |  NULL     | Lalala@            | Lorem ipsum bla-bla-bla |
      |  Nikita   | asd1d1dd"yasjjd.ru | Lorem ipsum bla-bla-bla |


  Scenario: Contact us with valid data
    Given Contact us page is open
    When Enter contact "kozkoznik25@yandex.ru"
    And Enter your name "Nikita"
    And Enter feedback "I'm almost done"
    And Resolve captcha
    And Click Send button
    Then Get approval message