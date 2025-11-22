from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_fi(driver):

    # Find gd
    time.sleep(5)

    # Create an ActionChains object
    actions = ActionChains(driver)

    for _ in range(12):
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.5)

    actions.send_keys(Keys.ENTER).perform()

    # Click on fi submitted
    time.sleep(5)

    actions.send_keys(Keys.ESCAPE).perform()
    time.sleep(0.25)
