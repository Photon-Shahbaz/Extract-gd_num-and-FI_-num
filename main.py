from selenium import webdriver
import login, gd, popUp_window, gui, gd_popup

def psw():

    # keeps chrome open
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize the browser window
    driver.maximize_window()

    # Perform functions
    login.login(driver)
    gd.extract_gd(driver)
    new_entries = gd.extract_rows(driver)
    # popUp_window.popup_win(new_entries)
    gd_popup.extract_from_popup(driver)
    gui.popup_win(new_entries)


psw()
