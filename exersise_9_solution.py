# Importing the Windows Speech API module
import win32com.client

# List of names to be spoken
names = [
    "stupidprogramm1",
    "Aayushgarg15",
    "yonik",
    "Niteshupadyay2",
    "Rameshkumar69"
]

# Creating a speech engine object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Iterating through each name in the list
for name in names:
    # Speaking a shoutout for the current name
    speaker.Speak(f"Shoutout to {name}.")
