#trying to create my own Piracy bot using PyAutoGUI
import pyautogui
import time
import random
import sys

# Wait for 5 seconds to set up proper browser tab before starting
time.sleep(5)

while True: 

    # Get the current mouse cursor's X and Y positions
    x, y = pyautogui.position()

    # Print the coordinates
    print(f"The current mouse position is X: {x} Y: {y}")
    # -602, 451
    # -1692, 535

    #pyautogui.click(-602,451)
    #time.sleep(2)
    #pyautogui.click(-1692, 535)
    #time.sleep(2)
    #pyautogui.click(-602,451)
    #time.sleep(2)

    # Wait for 150 seconds before starting again
    print("Begin waiting time of 2m30sec")
    time.sleep(150)