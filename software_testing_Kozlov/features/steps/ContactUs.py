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


@given("The PHPTravels is open")
def open_website(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.phptravels.net")
    context.driver.maximize_window()
    assert context.driver.title == "PHPTRAVELS - PHPTRAVELS"
    sleep(2)


@given('Contact us page is open')
def step_impl(context):
    sleep(1)
    context.driver.execute_script("window.scrollTo(0, 5800)")
    sleep(2)
    context.driver.find_element_by_xpath("/html/body/section[10]/div[1]/div[1]/div[1]/div/ul/li[3]/a").click()
    assert context.driver.title == "Contact - PHPTRAVELS"


@when('Enter contact "{email}"')
def step_impl(context, email):
    if email == "NULL":
        email = ""
    else:
        email = email
    context.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div/input').send_keys(email)


@step('Enter your name "{name}"')
def step_impl(context, name):
    if name == "NULL":
        name = ""
    else:
        name = name
    context.driver.find_element(By.NAME, "name").send_keys(name)


@step('Enter feedback "{message}"')
def step_impl(context, message):

    context.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div/div[2]/div[2]/form/div[3]/div/div/textarea').send_keys(message)
    sleep(1)


@step('Resolve captcha')
def step_captcha(context):
    element = context.driver.find_element(By.XPATH, '//*[@id="button"]')
    context.driver.execute_script("arguments[0].removeAttribute('disabled')", element)
    sleep(2)

@step('Click Send button')
def step_button(context):
    context.driver.execute_script("window.scrollTo(0, 200)")
    sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="button"]').click()
    sleep(2.5)


@then('Get error message')
def step_error(context):
    element = context.driver.find_element_by_xpath("/html/body/section[2]/div/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/input")
    x = element.get_attribute("validationMessage")
    if len(x) == 0:
        element = context.driver.find_element_by_xpath("/html/body/section[2]/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div/input")
        x = element.get_attribute("validationMessage")
        if len(x) == 0:
            element = context.driver.find_element_by_xpath("/html/body/section[2]/div/div/div[1]/div/div[2]/div[2]/form/div[3]/div/div/textarea")
            x = element.get_attribute("validationMessage")
    else:
        assert len(x) > 0


@then('Get approval message')
def step_approval(context):
    assert context.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div/div[2]/div[1]').is_displayed
    sleep(2)



