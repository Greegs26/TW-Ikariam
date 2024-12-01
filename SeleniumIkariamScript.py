from selenium import webdriver

# Initialize the Edge WebDriver
driver = webdriver.Edge()

# Open Ikariam
driver.get("https://www.ikariam.org")
driver.maximize_window()
print("Ikariam browser opened!")

# Keep the browser open until user presses Enter
input("Press Enter to close the browser")
driver.quit()

