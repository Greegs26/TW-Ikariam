#trying to create my own Piracy bot using PyAutoGUI
import pyautogui
import time
import random
import sys

coords=[(-606, 331), (-1009, 283), (-1158, 362), (-1276, 421), (-1465, 512), (-1506, 708), (-1191, 726)]

# Wait for 5 seconds to set up proper browser tab before starting
time.sleep(5)

while True: 

    # Get the current mouse cursor's X and Y positions
    x, y = pyautogui.position()

    # Print the coordinates
    print(f"The current mouse position is X: {x} Y: {y}")
    #The current mouse position is X: -606 Y: 331
    #The current mouse position is X: -1009 Y: 283
    #The current mouse position is X: -1158 Y: 362
    #The current mouse position is X: -1276 Y: 421
    #The current mouse position is X: -1465 Y: 512
    #The current mouse position is X: -1506 Y: 708
    #The current mouse position is X: -1191 Y: 726
    time.sleep(2)

    pyautogui.click(-616, 724)
    time.sleep(2)
    pyautogui.click(-1692, 535)
    time.sleep(2)
    pyautogui.click(-288, 484)
    time.sleep(2)
    #pyautogui.click(-775, 530)
    #time.sleep(2)
    pyautogui.click(-287, 573)
    time.sleep(2)

    pyautogui.click(-646, 651)
    time.sleep(2)
    #Selecting boats, Type the number 5000
    pyautogui.write('5000', interval=0.1)
    time.sleep(2)

    # -645, 653
    pyautogui.click(-159, 656)
    time.sleep(2)
    pyautogui.click(-254, 165)
    time.sleep(2)
    pyautogui.click(-85, 251)
    time.sleep(2)
    # Wait for 150 seconds before starting again
    print("Begin Pillage")
    time.sleep(9600)