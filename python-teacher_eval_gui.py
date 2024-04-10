from pynput import keyboard
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
    with keyboard.Controller() as controller:
        for key in keys:
            controller.press(key)
            controller.release(key)
            time.sleep(0.1)

def toggle_loop():
    global looping
    looping = not looping

def on_press(key):
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            pass
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            pass
        elif key == keyboard.Key.f1:
            toggle_loop()
        elif key == keyboard.Key.f2:
            toggle_loop()
        elif key == keyboard.Key.f3:
            toggle_loop()
        elif key == keyboard.Key.f4:
            toggle_loop()
        elif key == keyboard.Key.f5:
            toggle_loop()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    if looping:
        if keyboard.Key.ctrl_l in listener.pressed_keys or keyboard.Key.ctrl_r in listener.pressed_keys:
            if keyboard.Key.shift_l in listener.pressed_keys or keyboard.Key.shift_r in listener.pressed_keys:
                if keyboard.Key.f1 in listener.pressed_keys:
                    send_keys(['tab', 'space'] * 9 + ['tab'] * 3)
                elif keyboard.Key.f2 in listener.pressed_keys:
                    send_keys(['tab', 'right'] * 9 + ['tab'] * 3)
                elif keyboard.Key.f3 in listener.pressed_keys:
                    send_keys(['tab', 'right', 'right'] * 9 + ['tab'] * 3)
                elif keyboard.Key.f4 in listener.pressed_keys:
                    send_keys(['tab', 'right', 'right', 'right'] * 9 + ['tab'] * 3)
                elif keyboard.Key.f5 in listener.pressed_keys:
                    send_keys(['tab', 'right', 'right', 'right', 'right'] * 9 + ['tab'] * 3)
    time.sleep(0.1)
