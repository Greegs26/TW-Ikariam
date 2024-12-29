from selenium import webdriver
import time

# Set up options to keep the browser window open
options = webdriver.FirefoxOptions()
options.set_preference("browser.tabs.remote.autostart", False)  # Disable multi-process for easier debugging
options.set_preference("browser.tabs.warnOnClose", True)      # Warn before closing
options.set_preference("browser.link.open_newwindow", 3)      # Open new windows in new tabs

# Initialize the Firefox WebDriver with these options
driver = webdriver.Firefox(options=options)

# Open Ikariam
driver.get("https://www.ikariam.org")
driver.maximize_window()
print("Ikariam browser opened!")

time.sleep(60)  # wait for 60 seconds before continuing with script




