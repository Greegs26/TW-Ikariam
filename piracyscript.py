#trying to create my own Piracy bot using PyAutoGUI
import pyautogui
import time
import random
import sys

# Wait for 5 seconds to set up proper browser tab before starting
time.sleep(5)

while True: 

    # Get the current mouse cursor's X and Y positions
    #x, y = pyautogui.position()

    # Print the coordinates
    #print(f"The current mouse position is X: {x} Y: {y}")
    # -246, 656
    # -138, 681

    x=-199
    y=602

    pyautogui.click(x,y)
    print(f"Clicked at position X: {x} Y: {y}")

    # Wait for 170 to 180 seconds before starting
    wait_time=random.randint(170, 180)
    time.sleep(wait_time)