import pyautogui
import time
import random
import sys

# Initialize an empty list to store coordinates
coords = []

# Function to capture mouse coordinates
def capture_coordinates():
    print("Move your mouse to the desired position and press 'Enter' to capture coordinates.")
    print("Press 'q' and 'Enter' to finish capturing.")
    while True:
        input_key = input("Press 'Enter' to capture, or 'q' to quit: ")
        if input_key.lower() == 'q':
            print("Finished capturing coordinates.")
            break
        x, y = pyautogui.position()
        coords.append((x, y))
        print(f"Captured: {x}, {y}")

# Prompt to capture coordinates or use predefined ones
choice = input("Would you like to capture new coordinates? (y/n): ").strip().lower()
if choice == 'y':
    capture_coordinates()
else:
    # Default hardcoded coordinates
    coords = [
        (5042, 473), (4939, 557), (4978, 613), (5013, 662), 
        (5004, 750), (5141, 730), (5151, 624), (5533, 561), 
        (5441, 484), (5343, 458), (5242, 419), (5111, 430)
    ]

# Confirm the coordinates to be used
print(f"Using the following coordinates: {coords}")

# Index for cycling through coordinates
index = 0


# Wait for 5 seconds to set up proper browser tab before starting
time.sleep(5)

while True: 

    #This is used to click on actual city
    coord = coords[index]
    pyautogui.click(coord[0], coord[1])
    time.sleep(2)

    #used to click on pillage button
    pyautogui.click(2149, 767)
    time.sleep(2)

    #Sending max mortars
    pyautogui.click(3546, 799)
    time.sleep(2)
    #pyautogui.write('500', interval=0.1)
    #time.sleep(2)

    #used to click on spearmen
    pyautogui.click(3709, 752)
    time.sleep(2)
    #Selecting spearmen, Type the number 7
    pyautogui.write('7', interval=0.1)
    time.sleep(2)
  
    #Selecting boats
    pyautogui.click(3198, 872)
    time.sleep(2)
    #Selecting boats, Type the number 5000
    pyautogui.write('5000', interval=0.1)
    time.sleep(2)
    #Send pillage
    pyautogui.click(3680, 876)
    time.sleep(2)
    #Select Military Advisor
    pyautogui.click(3583, 425)
    time.sleep(2)
    #Exit Military Advisor
    pyautogui.click(2137, 533)
    time.sleep(2)


    # Wait for 150 seconds before starting again
    print("Begin Pillage - wait time of 60mins")
    time.sleep(3600)

    index = (index+1) % len(coords)