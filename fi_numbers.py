from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def extract_fi(driver):

    # Wait for table to render
    tbody_xpath = '//*[@id="root"]/div[3]/div[5]/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/table/tbody'

    tbody = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, tbody_xpath))
    )

    # Find all rows inside tbody
    rows = tbody.find_elements(By.TAG_NAME, "tr")

    extracted = []

    # Loop through first 5 data rows (if available)
    for i in range(min(5, len(rows))):
        cols = rows[i].find_elements(By.TAG_NAME, "td")

        # Safety check → some rows might not have 8 columns
        if len(cols) < 8:
            continue

        col4 = cols[3].text.strip()
        col5 = cols[4].text.strip()
        col7 = cols[6].text.strip()
        col8 = cols[7].text.strip()

        extracted.append([col4, col5, col7, col8])

    return extracted
