import pyautogui
import time

print("""
=========================================================================================
    Faculty Evaluation Google Forms Fill Upper-ization v.0.0.1'
    For Batch Syncytium and Dextera <3 Only. Intellectual Property of Syncytium'
    Instructions:
    1) Go to the Page with the Likert Scale (1-5)
    2) Press your desired score for all
    3) Press Ctrl + Shift + [F1,F2,F3,F4,F5] TWICE depending on your desired score
    4) Press Next (shortcut is space)
    5) Repeat
=========================================================================================
    """)

looping = False

def send_keys(keys):
    print(f"Executing (0.1s delay)")
    time.sleep(1.5)
    for key in keys:
        pyautogui.press(key)
        time.sleep(0.1)

def toggle_loop():
    global looping
    looping = not looping

while True:
    if looping:
        if pyautogui.keyDown('ctrl') and pyautogui.keyDown('shift') and pyautogui.keyDown('f1'):
            send_keys(['tab', 'space'] * 9 + ['tab'] * 3)
        elif pyautogui.keyDown('ctrl') and pyautogui.keyDown('shift') and pyautogui.keyDown('f2'):
            send_keys(['tab', 'right'] * 9 + ['tab'] * 3)
        elif pyautogui.keyDown('ctrl') and pyautogui.keyDown('shift') and pyautogui.keyDown('f3'):
            send_keys(['tab', 'right', 'right'] * 9  + ['tab'] * 3)
        elif pyautogui.keyDown('ctrl') and pyautogui.keyDown('shift') and pyautogui.keyDown('f4'):
            send_keys(['tab', 'right', 'right', 'right'] * 9 + ['tab'] * 3)
        elif pyautogui.keyDown('ctrl') and pyautogui.keyDown('shift') and pyautogui.keyDown('f5'):
            send_keys(['tab', 'right', 'right', 'right', 'right'] * 9 + ['tab'] * 3)
    time.sleep(0.1)
