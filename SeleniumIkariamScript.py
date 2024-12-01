from selenium import webdriver
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open Ikariam
driver.get("https://www.ikariam.org")
driver.maximize_window()
print("Ikariam browser opened!")

time.sleep(60) # wait for 60 seconds before continuing with scriot

# Keep the browser open until user presses Enter
input("Press Enter to close the browser")
driver.quit()



