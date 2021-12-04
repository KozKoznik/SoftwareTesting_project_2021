from behave import given, when, then, step
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from features.steps.locators import locator
from selenium.webdriver.common.keys import Keys
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)


@given("The PHPTravels page is open")
def open_website(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.phptravels.net")
    context.driver.maximize_window()
    assert context.driver.title == "PHPTRAVELS - PHPTRAVELS"
    sleep(2)


@given('Subscribe field is visible')
def step_visibility(context):
    context.driver.execute_script("window.scrollTo(0, 4000)")
    sleep(2)
    assert context.driver.find_element(By.XPATH, '//*[@id="exampleInputEmail1"]').is_displayed()


@when('Enter "{email}"')
def step_email(context, email):
    if email == 'NULL':
        email = ""
    else:
        email = email
    context.driver.find_element(By.XPATH, '//*[@id="exampleInputEmail1"]').send_keys(email)
    sleep(3)


@step('Subscribe button is clicked')
def step_button(context):
    context.driver.find_element(By.XPATH, '//*[@id="email_subscribe"]').click()


@then('Get error message "{msg}"')
def step_error(context, msg):
    #//div[text()="Please add correct email!"]
    message = str(msg)
    text = context.driver.find_element(By.XPATH, '//div[text()="'+message+'"]').text
    print(text)
    assert text == message
    sleep(2)


@then('Get approval message "Thank you for subscription"')
def step_error(context):
    #//div[text()="Please add correct email!"]
    message = "Thank you for subscription"
    text = context.driver.find_element(By.XPATH, '//div[text()="'+message+'"]').text
    print(text)
    assert text == message
    sleep(2)



