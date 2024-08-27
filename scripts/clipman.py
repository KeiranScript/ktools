import pyperclip
import keyboard
import time
import os
import sys
import subprocess

# Clipboard history file path
CLIPBOARD_HISTORY_FILE = os.path.expanduser("~/.clipboard_history.txt")


def check_and_elevate_privileges():
    """Check if the script is being run as root. If not, elevate privileges using sudo."""
    if os.geteuid() != 0:
        print(
            "This script requires root privileges to access certain system resources."
        )
        try:
            subprocess.check_call(["sudo", sys.executable] + sys.argv)
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("Failed to obtain root privileges. Exiting.")
            sys.exit(1)


def save_clipboard_to_history(clipboard_content):
    """Save the current clipboard content to the history file."""
    with open(CLIPBOARD_HISTORY_FILE, "a") as f:
        f.write(clipboard_content + "\n")


def load_clipboard_history():
    """Load the clipboard history from the file."""
    if os.path.exists(CLIPBOARD_HISTORY_FILE):
        with open(CLIPBOARD_HISTORY_FILE, "r") as f:
            return f.read().splitlines()
    return []


def display_clipboard_history():
    """Display the clipboard history."""
    history = load_clipboard_history()
    for idx, entry in enumerate(history):
        # Display first 50 characters of each entry
        print(f"{idx + 1}: {entry[:50]}")


def main():
    check_and_elevate_privileges()

    print("Starting Clipboard Manager...")
    clipboard_history = load_clipboard_history()

    try:
        while True:
            # Check for new clipboard content
            clipboard_content = pyperclip.paste()
            if clipboard_history == [] or clipboard_content != clipboard_history[-1]:
                clipboard_history.append(clipboard_content)
                save_clipboard_to_history(clipboard_content)
                print(f"New entry added to clipboard history: {
                      clipboard_content[:50]}")

            # Check for the 'Ctrl+Shift+V' shortcut to display clipboard history
            if keyboard.is_pressed("ctrl+shift+v"):
                print("\nClipboard History:")
                display_clipboard_history()

                # Allow user to select a previous entry
                selection = input(
                    "\nEnter the number of the entry to copy to clipboard, or press Enter to cancel: "
                )
                if selection.isdigit():
                    idx = int(selection) - 1
                    if 0 <= idx < len(clipboard_history):
                        pyperclip.copy(clipboard_history[idx])
                        print(f"Copied to clipboard: {
                              clipboard_history[idx][:50]}")

                time.sleep(1)  # Small delay to prevent multiple triggers
            time.sleep(0.5)  # Polling interval

    except KeyboardInterrupt:
        print("Clipboard Manager terminated.")


if __name__ == "__main__":
    main()
