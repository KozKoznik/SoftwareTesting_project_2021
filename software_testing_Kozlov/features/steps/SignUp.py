from behave import given, when, then, step
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from features.steps.locators import locator
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)


@given("The PHPTravels sign up page is open")
def open_website(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.phptravels.net/signup")
    context.driver.maximize_window()
    assert context.driver.title == "Signup - PHPTRAVELS"


@given("Sign up page is open")
def open_website(context):
    assert context.driver.title == "Signup - PHPTRAVELS"


@when('Enter email "{email}"')
def step_impl(context, email):
    context.driver.find_element(*locator["sign_up_email"]).send_keys(email)


@step('The user has a first name of "{name}"')
def step_impl(context, name):
    context.driver.find_element(By.NAME, "first_name").send_keys(name)


@step('The user has a last name of "{surname}"')
def step_impl(context, surname):
    context.driver.find_element(By.NAME, "last_name").send_keys(surname)


@step('Phone is "{phone}"')
def step_impl(context, phone):
    context.driver.find_element(By.NAME, "phone").send_keys(phone)


@step('Password of "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.NAME, "password").send_keys(password)


@step('Signup button is clicked')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 500)")
    sleep(1)
    context.driver.find_element(*locator["create_account_button"]).click()


@then("The account creation is successful")
def step_impl(context):
    sleep(1)
    assert context.driver.find_element(By.CSS_SELECTOR, ".signup").is_displayed()
    assert context.driver.title == "Login - PHPTRAVELS"


@then("The user gets the message that user already exist")
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-danger").is_displayed()
    sleep(1)
