from selenium import webdriver
import time

# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

# Open Ikariam
driver.get("https://www.ikariam.org")
driver.maximize_window()
print("Ikariam browser opened!")

time.sleep(60) # wait for 60 seconds before continuing with script

# Keep the browser open until user presses Enter
input("Press Enter to close the browser")
driver.quit()



