# Import the os module to execute PowerShell commands
import os

# Import the time module to pause the program between reminders
import time

# Import ctypes to access Windows API functions such as MessageBox
import ctypes

# Import threading (currently not used in this program)
import threading

# Time interval (in seconds) between reminders
# Example:
# 10    -> every 10 seconds
# 60    -> every 1 minute
# 3600  -> every 1 hour
REPEAT_INTERVAL = 10


# Define a function that reminds the user to drink water
def remind():

    # Use PowerShell's text-to-speech feature to speak the reminder
    os.system(
        'powershell -Command "Add-Type -AssemblyName System.Speech;'
        '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;'
        '$speak.Speak(\'Hey Ganesh, drink water\')"'
    )

    # Display a Windows popup message
    ctypes.windll.user32.MessageBoxW(
        0,                              # No parent window
        "Hey Ganesh, Drink water!",     # Message
        "Reminder",                     # Window title
        0x40 | 0x1                      # Information icon + OK button
    )


# Run the reminder forever
while True:

    # Call the reminder function
    remind()

    # Wait for the specified interval before showing the next reminder
    time.sleep(REPEAT_INTERVAL)
