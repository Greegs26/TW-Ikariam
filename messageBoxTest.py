import pyautogui

pyautogui.alert("Test message.", "Alert Title")

choice = pyautogui.confirm("Are you sure?", "Confirmation", ["Yes", "No"])
if choice == "Yes":
    print("User confirmed")