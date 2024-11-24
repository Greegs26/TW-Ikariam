#Creating Mechquest bot using pythong
import pyautogui
import time
import random
import sys

time.sleep(2)
while True: 

    # Get the current mouse cursor's X and Y positions
    # x, y = pyautogui.position()

    # Print the coordinates
    # print(f"The current mouse position is X: {x} Y: {y}")
    # time.sleep(1)
    # 3561, 756
    # battle start
    
    # find the spider
    pyautogui.click(3561, 756)
    time.sleep(8)

    # battle start
    pyautogui.click(2886, 500)
    time.sleep(9)
    pyautogui.click(2886, 554)
    time.sleep(9)
    pyautogui.click(2886, 600)
    time.sleep(9)
    pyautogui.click(2886, 649)
    time.sleep(9)
    pyautogui.click(2886, 698)
    time.sleep(9)
    pyautogui.click(2886, 756)
    time.sleep(9)

    # End the battle
    pyautogui.click(3018, 663)
    time.sleep(3)
    pyautogui.click(2887, 755)
    time.sleep(3)