# form_filling.py

from selenium.webdriver.common.by import By
import time

def fill_form(driver):
    try:
        # Click the "Apply now" button
        apply_button = driver.find_element(By.XPATH, "//div[@class='buttons_container']//button[contains(text(), 'Apply now')]")
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", apply_button)
        time.sleep(1)
        apply_button.click()

        # Click the "Proceed to application" button after redirection
        proceed_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'proceed-btn') and text()='Proceed to application']"))
        )
        proceed_button.click()

        # Locate the resume upload component and upload the file
        upload_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='custom_resume']"))
        )
        upload_label.click()
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "custom_resume"))
        )
        file_input.send_keys("scraper\5.pdf")  # Update with your file path

        print("Form filled and resume uploaded!")
    except Exception as e:
        print("Error in form filling:", e)
