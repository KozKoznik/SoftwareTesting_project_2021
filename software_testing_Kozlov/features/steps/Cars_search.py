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


@given("The PHPTravels main page is open")
def open_website(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.phptravels.net")
    context.driver.maximize_window()
    assert context.driver.title == "PHPTRAVELS - PHPTRAVELS"
    sleep(2)


@given('Tab cars is open')
def step_impl(context):
    context.driver.find_element(*locator["cars_tab"]).click()


@when('Enter departure city "{city}"')
def step_impl(context, city):
    context.driver.find_element(By.XPATH, '//*[@id = "select2-carfrom-container"]').click()
    context.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(city)
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)
    sleep(1)


@step('Enter arrival city "{city2}"')
def step_impl(context, city2):
    context.driver.find_element(By.CSS_SELECTOR, ".col-md-5 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1)").click()
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(city2)
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)


@step('Choose departure date "{date}"')
def step_impl(context, date):
    element = context.driver.find_element(By.XPATH, "//*[@id='datefrom']")
    element.click()
    sleep(1)
    if int(date) > 9:
        value = f"{date}-12-2021"
        context.driver.execute_script("arguments[0].setAttribute('value',arguments[1])", element, value)
    else:
        value = f"0{date}-12-2021"
        context.driver.execute_script("arguments[0].setAttribute('value',arguments[1])", element, value)


@step('Choose last date "{date2}"')
def step_impl(context, date2):
    element = context.driver.find_element(By.XPATH, "//*[@id='dateto']")
    element.click()
    sleep(1)
    if int(date2) > 9:
        value = f"{date2}-12-2021"
        context.driver.execute_script("arguments[0].setAttribute('value',arguments[1])", element, value)
    else:
        value = f"0{date2}-12-2021"
        context.driver.execute_script("arguments[0].setAttribute('value',arguments[1])", element, value)


@step('Choose amount of adults "{adults}"')
def step_impl(context, adults):
    context.driver.find_element(By.XPATH, "//*[@id='cars-search']//a[@class='dropdown-toggle dropdown-btn travellers waves-effect']").click() #find
    element = context.driver.find_element(By.XPATH, "//*[@id='cars-search']//i[@class='la la-plus']")
    y=int(adults)
    x=1
    while x < y:
        element.click()
        x=x+1


@step('Search button is clicked')
def step_impl(context):
    sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id='cars']//*[@id='submit']").click()


@then("Page with cars will open")
def step_impl(context):
    assert context.driver.title == "Cars in - PHPTRAVELS"
    sleep(2)


