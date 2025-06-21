import threading
import importlib
import time
import run_bot_selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def run_command(driver):
    print("Running Piracy script")
    importlib.reload(run_bot_selenium)
    threading.Thread(target=run_bot_selenium.run_click_bot, args=(driver,), daemon=True).start()

def dummy_action():
    print("This is another action")

def quit_program():
    print("Quitting program...")
    for d in drivers.values():
        d.quit()
    global running
    running = False

command_map = {
    "piracy": run_command,
    "dummy": dummy_action,
    "quit": quit_program,
    # Add more commands here
}

def print_available_commands():
    print("\nAvailable commands:")
    for cmd in command_map:
        print(f" - {cmd}")
    print() # Extra line for spacing

def wait_for_new_tab(driver, timeout=60):
    # Waits for a new tab to open for the given driver and switches to it
    original_tabs = driver.window_handles
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: len(d.window_handles) > len(original_tabs)
        )
        new_tab = list(set(driver.window_handles) - set(original_tabs))[0]
        driver.switch_to.window(new_tab)
        print("Switched to new tab")
    except TimeoutException:
        print("No new tab opened whithin timeout")
        return None

def command_listener():
    global running
    running = True
    while running:
        cmd = input("Type a command: ").strip().lower()
        action = command_map.get(cmd)     
        
        if not action:
            print(f"Unknown command: {cmd}")

        # Only ask for driver if this command expects one
        if cmd not in ["quit"]: # Commands that don't need a driver
            driver_key = input("Which driver? (1 to 6): ").strip()
            driver = drivers.get(driver_key)
            if driver:
                action(driver)
            else:
                print(f"Unknown driver: {driver_key}")
        
        else:
            action()  


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# OPTIONAL: specify path to geckodriver if not in PATH
# service = Service(executable_path="/path/to/geckodriver")

# Setup Firefox options
options = Options()
options.set_preference("dom.webnotifications.enabled", False)  # Disable popups
options.set_preference("dom.webdriver.enabled", False) # Hides navigator.webdriver

# Ask user how many drivers to open
try:
    num_sessions = int(input("How many browser sessions would you like to open? (1 to 6): ").strip())
    if not (1 <= num_sessions <= 6):
        raise ValueError
except ValueError:
    print("Invalid input. Defaulting to 1 session.")
    num_sessions = 1

# Launch only the requested number of drivers
drivers = {}

for i in range(1, num_sessions + 1):
    print(f"\nLaunching session {i}...")
    driver = webdriver.Firefox(options=options)
    driver.get("https://ikariam.org")
    
    print("Please select your account and wait for the new tab to open.")
    wait_for_new_tab(driver)

    drivers[str(i)] = driver
    print(f"Session {i} is ready.")

print_available_commands() # Show command options here
command_listener()







