#trying to create my own Piracy bot using PyAutoGUI
import pyautogui
import time
import random
import sys

#The current mouse position is X: -321 Y: 460
#The current mouse position is X: -543 Y: 433
#The current mouse position is X: -625 Y: 483
#The current mouse position is X: -686 Y: 515
#The current mouse position is X: -794 Y: 563
#The current mouse position is X: -816 Y: 672
#The current mouse position is X: -641 Y: 682

#The current mouse position is X: -360 Y: 691
#The current mouse position is X: -269 Y: 668
#The current mouse position is X: -271 Y: 599
#The current mouse position is X: -386 Y: 540
#The current mouse position is X: -284 Y: 543
coords=[(5042, 473), (4939, 557), (4978, 613), (5013, 662), (5004, 750), (5141, 730), (5151, 624), (5533, 561), (5441, 484), (5343, 458), (5242, 419), (5111, 430)]
index=8

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
    pyautogui.click(5624, 526)
    time.sleep(2)
    #Selecting spearmen, Type the number 7
    pyautogui.write('7', interval=0.1)
    time.sleep(2)
    #Sending max mortars
    pyautogui.click(5631, 758)
    time.sleep(2)
    pyautogui.write('500', interval=0.1)
    time.sleep(2)
    #Selecting boats
    pyautogui.click(5119, 882)
    time.sleep(2)
    #Selecting boats, Type the number 5000
    pyautogui.write('5000', interval=0.1)
    time.sleep(2)
    #Send pillage
    pyautogui.click(5598, 874)
    time.sleep(2)
    #Select Military Advisor
    pyautogui.click(5508, 146)
    time.sleep(2)
    #Exit Military Advisor
    pyautogui.click(4050,262)
    time.sleep(2)


    # Wait for 150 seconds before starting again
    print("Begin Pillage - wait time of 60mins")
    time.sleep(3600)

    index = (index+1) % len(coords)