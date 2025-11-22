from selenium.webdriver.common.by import By

import gd


def login(driver):
    # open website
    driver.get("https://app.psw.gov.pk/app/")
    # driver.implicitly_wait(0.5)

    # Find username, password locations
    username = driver.find_element(by=By.NAME, value="userName")
    password = driver.find_element(by=By.NAME, value="password")


    # Find Login button
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # Enter username, password & company code
    username.send_keys("UN-00-B372141")
    password.send_keys("66CtS2zFu%BNaP!")

    # Clicks on login button
    Login_button.click()
