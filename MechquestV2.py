#Creating Mechquest bot using pythong
import pyautogui
import time
import random
import sys

def attack():
    # attack
    n=0
    while n<5:
        pyautogui.click(4725, 533)
        time.sleep(3)
        n=n+1
    pyautogui.click(4725, 469)
    time.sleep(3)
    pyautogui.click(4937, 671)
    time.sleep(3)
    # collect level up
    #pyautogui.click(4797, 785)
    #time.sleep(2)

def right_side():
    # click right side of screen
    pyautogui.click(5485, 227)
    time.sleep(4)
    pyautogui.click(5485, 227)
    time.sleep(4)

def next():
    n=0
    while n<=30:
        pyautogui.click(5368, 810)
        time.sleep(0.1)
        n=n+1
    time.sleep(2)

def top_side():
    pyautogui.click(4769, 59)
    time.sleep(3)

while True:
    time.sleep(2)

    # find event
    pyautogui.click(5224, 447)
    time.sleep(2)

    # next, talk with headmaster
    next()

    # Big NEXT
    pyautogui.click(4826, 600)
    time.sleep(2)

    # next, in crystal cave
    next()

    # EQUIP THE WEAPON + Enter the Cave
    pyautogui.click(4807, 696)
    time.sleep(1)
    pyautogui.click(4807, 696)
    time.sleep(2)

    # click right side of screen
    right_side()

    # attack
    attack()

    # click right side of screen
    right_side()

    # attack
    attack()

    # click right side of screen
    right_side()

    # attack
    attack()

    # ((long)) click right side of screen
    pyautogui.click(5485, 227)
    time.sleep(10)

    # click right side of screen
    right_side()

    # attack
    attack()

    # click right side of screen
    right_side()

    # click top side of screen
    top_side()

    # attack
    attack()

    # click top side of screen
    top_side()

    # click top side of screen
    top_side()

    # attack
    attack()

    # click top side of screen
    top_side()

    # click top side of screen
    top_side()

    # next, talking to tree
    next()

    # ((long)) click top side of screen
    pyautogui.click(4813, 113)
    time.sleep(2)

    # next, talking to dean
    next()

    # oh no
    pyautogui.click(4813, 723)
    time.sleep(2)

    # back
    pyautogui.click(5328, 966)
    time.sleep(2)

    # next, talking to ghost
    next()

    # complete!
    pyautogui.click(4823, 693)
    time.sleep(2)
    pyautogui.click(4798, 759)
    time.sleep(2)


