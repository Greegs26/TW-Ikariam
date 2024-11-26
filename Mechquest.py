#Creating Mechquest bot using python
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
    pyautogui.click(1372, 631)
    time.sleep(8)

    # battle start
    pyautogui.click(930, 467)
    time.sleep(9)
    pyautogui.click(930, 637)
    time.sleep(9)
    pyautogui.click(930, 502)
    time.sleep(9)
    pyautogui.click(930, 467)
    time.sleep(9)    

    # End the battle
    pyautogui.click(1021, 574)
    time.sleep(3)
    pyautogui.click(941, 636)
    time.sleep(3)