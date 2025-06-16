import threading
import importlib
import time
from run_bot_selenium import run_click_bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_command():
    print("Running Piracy script")
    importlib.reload(run_bot_selenium)
    threading.Thread(target=run_bot.run_click_bot, daemon=True).start()

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

# Store current number of tabs
num_tabs_before = len(driver1.window_handles)

# Wait until the number of tabs increases
WebDriverWait(driver1, 10).until(
    lambda d: len(d.window_handels) > num_tabs_before
)
# Switch to the new tab
driver1.switch_to.window(driver1.window_handles[-1])
print("Switched to new tab")

print_available_commands() # Show command options here
command_listener()







