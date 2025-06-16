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
    driver1.quit()
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

def wait_for_new_tab(driver, timeout=60)
    # Waits for a new tab to open for the given driver and switches to is
    original_tabs = driver.window_handles
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: len(d.window_handles) > len(original_tabs)
        )
        new_tab = list(set(driver.window_handles) - set(original_tabs))[0]
        driver.switch_to.winder(new_tab)
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
        if action:
            action()
        else:
            print(f"Unknown command: {cmd}")


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# OPTIONAL: specify path to geckodriver if not in PATH
# service = Service(executable_path="/path/to/geckodriver")

# Setup Firefox options
options = Options()
options.set_preference("dom.webnotifications.enabled", False)  # Disable popups

# Start browser
driver1 = webdriver.Firefox(options=options)  # , service=service if needed
driver1.get("https://ikariam.org")
wait_for_new_tab(driver1)

print_available_commands() # Show command options here
command_listener()







