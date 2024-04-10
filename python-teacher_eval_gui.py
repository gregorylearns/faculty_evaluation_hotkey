import keyboard
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
        keyboard.send(key)
        time.sleep(0.1)

def toggle_loop():
    global looping
    looping = not looping

keyboard.add_hotkey('ctrl+shift+f1', lambda: toggle_loop())
keyboard.add_hotkey('ctrl+shift+f2', lambda: toggle_loop())
keyboard.add_hotkey('ctrl+shift+f3', lambda: toggle_loop())
keyboard.add_hotkey('ctrl+shift+f4', lambda: toggle_loop())
keyboard.add_hotkey('ctrl+shift+f5', lambda: toggle_loop())

while True:
    if looping:
        if keyboard.is_pressed('ctrl+shift+f1'):
            send_keys(['tab', 'space'] * 9 + ['tab'] * 3)
        elif keyboard.is_pressed('ctrl+shift+f2'):
            send_keys(['tab', 'right'] * 9 + ['tab'] * 3)
        elif keyboard.is_pressed('ctrl+shift+f3'):
            send_keys(['tab', 'right', 'right'] * 9  + ['tab'] * 3)
        elif keyboard.is_pressed('ctrl+shift+f4'):
            send_keys(['tab', 'right', 'right', 'right'] * 9 + ['tab'] * 3)
        elif keyboard.is_pressed('ctrl+shift+f5'):
            send_keys(['tab', 'right', 'right', 'right', 'right'] * 9 + ['tab'] * 3)
    time.sleep(0.1)
