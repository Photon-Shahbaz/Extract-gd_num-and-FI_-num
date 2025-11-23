from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_from_popup(driver):

    main_window = driver.current_window_handle  # Save main window handle

    # Switch to iframe
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "frame"))
    )

    # 1️⃣ Click the link that opens popup window
    link = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder2_dgSubmitted_ctl02_lbView"]')
    link.click()

    # 2️⃣ Wait for new popup window to appear
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    # 3️⃣ Switch to popup window
    for window in driver.window_handles:
        if window != main_window:
            popup_window = window
            break

    driver.switch_to.window(popup_window)

    # 4️⃣ Extract text from popup
    consignor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="GdImportViewUc1_lblConsignorName"]'))
    ).text.strip()

    print("Extracted Consignor Name:", consignor)

    # 5️⃣ Close popup
    driver.close()

    # 6️⃣ Switch back to main window
    driver.switch_to.window(main_window)

    return consignor
