from selenium.webdriver.common.by import By

locator = {
    "sign_up_email": (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/div/input"),
    "login_email": (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input"),
    "create_account_button": (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[7]/button"),
    "login_button": (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/button"),
    "cars_tab": (By.CSS_SELECTOR, "#cars-tab"),


}
