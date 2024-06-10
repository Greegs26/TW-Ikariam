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
    # -774, 485
    # - 775, 530
    # - 775, 574
    # -1129, 652
    time.sleep(2)

    #pyautogui.click(-602,451)
    #time.sleep(2)
    pyautogui.click(-1692, 535)
    time.sleep(2)
    pyautogui.click(-774, 485)
    time.sleep(2)
    pyautogui.click(-775, 530)
    time.sleep(2)
    pyautogui.click(-775, 574)
    time.sleep(2)

    pyautogui.click(-1129, 652)
    time.sleep(2)
    #Type the number 5000
    pyautogui.write('5000', interval=0.1)
    time.sleep(2)

    # -645, 653
    pyautogui.click(-645, 653)
    time.sleep(2)
    pyautogui.click(-254, 165)
    time.sleep(2)
    # Wait for 150 seconds before starting again
    print("Begin Pillage")
    time.sleep(9600)