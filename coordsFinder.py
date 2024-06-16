#trying to create my own Piracy bot using PyAutoGUI
import pyautogui
import time
import random
import sys

time.sleep(5)
# Get the current mouse cursor's X and Y positions
while True:
    x, y = pyautogui.position()

    # Print the coordinates
    print(f"The current mouse position is X: {x} Y: {y}")
    # -602, 451
    # -1692, 535
    # -774, 485
    # - 775, 530
    # - 775, 574
    # -1129, 652

    #X: -616 Y: 724
    time.sleep(2)