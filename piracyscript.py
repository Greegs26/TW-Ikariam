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

    x=1729
    y=708

    # Start clicking with a random interval
    start_time=time.time()
    wait_time=random.randint(1,2)

    while time.time()-start_time<8:
        pyautogui.click(x,y)
        print(f"Clicked at position X: {x} Y: {y}")
        time.sleep(1)
        time.sleep(wait_time)

    # Wait for 450 seconds before starting again
    print("Begin waiting time of 7m30sec")
    time.sleep(450)