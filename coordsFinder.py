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
#The current mouse position is X: -321 Y: 460
#The current mouse position is X: -543 Y: 433
#The current mouse position is X: -625 Y: 483
#The current mouse position is X: -686 Y: 515
#The current mouse position is X: -794 Y: 563
#The current mouse position is X: -816 Y: 672
#The current mouse position is X: -641 Y: 682

    #X: -616 Y: 724
    time.sleep(2)