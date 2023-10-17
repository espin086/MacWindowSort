import time
import subprocess
import pyautogui


# Open the application
subprocess.call(["open", "-a", "Mail"])

# Wait for the application to open
time.sleep(1)

# Activate the application
pyautogui.hotkey("command", "tab")

# Wait for the application to become active
time.sleep(1)

# Press the shortcut Command + 1
pyautogui.hotkey("command", "1")
