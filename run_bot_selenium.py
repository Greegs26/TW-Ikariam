# run_bot_selenium.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_click_bot(driver):
    print("Running Selenium-based bot...")
    time.sleep(3)
    driver.find_element(By.ID, "js_cityLink").click()

    print("Bot actions complete.")