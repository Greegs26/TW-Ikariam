#trying to create my own Piracy bot using PyAutoGUI
import pyautogui
import time
import random
import sys

# Wait for 1 seconds to set up proper browser tab before starting
time.sleep(1)

# Initialize an empty list to store coordinates
coords = []

# Function to capture mouse coordinates
def capture_coordinates():
    print("Move your mouse to the desired position and press 'Enter' to capture coordinates.")
    print("Press 'q' and 'Enter' to finish capturing.")
    while True:
        input_key = input("Press 'Enter' to capture, or 'q' to quit: ")
        if input_key.lower() == 'q':
            print("Finished capturing coordinates.")
            break
        x, y = pyautogui.position()
        coords.append((x, y))
        print(f"Captured: {x}, {y}")

# Prompt to capture coordinates or use predefined ones
capture_coordinates()



# Confirm the coordinates to be used
print(f"Using the following coordinates: {coords}")

# Wait for 5 seconds to set up proper browser tab before starting
time.sleep(5)

while True:
    for coord in coords:
        pyautogui.click(coord[0], coord[1])
        time.sleep(2)

    print("Begin waiting period of 7m30s")
    time.sleep(470)

