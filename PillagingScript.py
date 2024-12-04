import pyautogui
import time
import random
import sys

coords=[(5042, 473), (4939, 557), (4978, 613), (5013, 662), (5004, 750), (5141, 730), (5151, 624), (5533, 561), (5441, 484), (5343, 458), (5242, 419), (5111, 430)] ##Coords for 97:7
## coords = [(4998, 460), (5033, 519), (4945, 584)] # Coords for 97:11
index=0

# Wait for 5 seconds to set up proper browser tab before starting
time.sleep(5)

while True: 

    #This is used to click on actual city
    coord = coords[index]
    pyautogui.click(coord[0], coord[1])
    time.sleep(2)

    #used to click on pillage button
    pyautogui.click(4072, 501)
    time.sleep(2)
    #used to click on spearmen
    pyautogui.click(5619, 432)
    time.sleep(2)
    #Selecting spearmen, Type the number 7
    pyautogui.write('7', interval=0.1)
    time.sleep(2)
    #Sending max mortars
    pyautogui.click(5622, 7482)
    time.sleep(2)
    pyautogui.write('500', interval=0.1)
    time.sleep(2)
    #Selecting boats
    pyautogui.click(5122, 559)
    time.sleep(2)
    #Selecting boats, Type the number 5000
    pyautogui.write('5000', interval=0.1)
    time.sleep(2)
    #Send pillage
    pyautogui.click(5598, 874)
    time.sleep(2)
    #Select Military Advisor
    pyautogui.click(5600, 553)
    time.sleep(2)
    #Exit Military Advisor
    pyautogui.click(4050,262)
    time.sleep(2)


    # Wait for 150 seconds before starting again
    print("Begin Pillage - wait time of 60mins")
    time.sleep(3600)

    index = (index+1) % len(coords)