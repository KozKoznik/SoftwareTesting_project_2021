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


@given("The PHPTravels login page is open")
def open_website(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.phptravels.net/login")
    context.driver.maximize_window()
    assert context.driver.title == "Login - PHPTRAVELS"


@given('Enter login "kozlov_example@email.com" and password ""')
def step_impl(context):
    context.driver.find_element(*locator["login_email"]).send_keys("kozlov_example@email.com")
    context.driver.find_element(By.NAME, "password").send_keys("")


@given('Enter login "kozlov_example2mail.ru" and password "38275293"')
def step_impl(context):
    context.driver.find_element(*locator["login_email"]).send_keys("kozlov_example2mail.ru")
    context.driver.find_element(By.NAME, "password").send_keys("38275293")


@given('Enter login "" and password "12984000"')
def step_impl(context):
    context.driver.find_element(*locator["login_email"]).send_keys("")
    context.driver.find_element(By.NAME, "password").send_keys("12984000")


@given('Enter login "Кириллица@yandex.ru" and password "98791054"')
def step_impl(context):
    context.driver.find_element(*locator["login_email"]).send_keys("Кириллица@yandex.ru")
    context.driver.find_element(By.NAME, "password").send_keys("98791054")


@when('Login button is clicked')
def step_impl(context):
    sleep(1)
    context.driver.find_element(*locator["login_button"]).click()
    sleep(2)


@then('Text error is shown')
def step_impl(context):
    sleep(2)
    element = context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input")
    x = element.get_attribute("validationMessage")
    if len(x) == 0:
        element = context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input")
        x = element.get_attribute("validationMessage")
    assert len(x) > 0


@given('Enter login "completelyrandomemail@email.com" and password "12JKJiis"')
def step_impl(context):
    context.driver.find_element(*locator["login_email"]).send_keys("completelyrandomemail@email.com")
    context.driver.find_element(By.NAME, "password").send_keys("12JKJiis")


@given('Enter login "kozlov_example@yandex.ru" and password "12984000"')
def step_impl(context):
    context.driver.find_element(*locator["login_email"]).send_keys("kozlov_example@yandex.ru")
    context.driver.find_element(By.NAME, "password").send_keys("12984000")


@then("User gets the message Wrong credentials")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]").is_displayed()
    sleep(1)


@then("Login is successful")
def step_impl(context):
    assert context.driver.title == "Dashboard - PHPTRAVELS"
    sleep(1)
