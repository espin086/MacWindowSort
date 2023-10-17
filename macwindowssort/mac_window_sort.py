import time
import subprocess
import pyautogui
import argparse


def activate_application_by_name(application_name):
    script = f'tell application "{application_name}" to activate'
    subprocess.call(["osascript", "-e", script])


def windows_sort(application, position):
    """Open an application and switch to a specific position."""
    # Open the application
    subprocess.call(["open", "-a", application])

    # Wait for the application to open
    time.sleep(0.05)

    # Activate the application
    activate_application_by_name(application)

    # Wait for the application to become active
    time.sleep(0.05)

    # Press the shortcut Command + position
    pyautogui.hotkey("command", str(position))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Open an application and switch to a specific position."
    )
    parser.add_argument("application", type=str, help="Name of the application to open")
    parser.add_argument(
        "position",
        type=int,
        choices=[1, 2, 3, 4, 5, 6],
        help="Position to switch to (1-6)",
    )

    args = parser.parse_args()
    windows_sort(args.application, args.position)
