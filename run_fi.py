from selenium import webdriver
import login, popUp_window, fi_page, fi_numbers, gui


def fi():

    # keeps chrome open
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize the browser window
    driver.maximize_window()

    # Perform functions
    login.login(driver)
    fi_page.click_fi(driver)
    new_fi = fi_numbers.extract_fi(driver)
    # popUp_window.popup_win(new_fi)
    gui.popup_win(new_fi)


fi()
