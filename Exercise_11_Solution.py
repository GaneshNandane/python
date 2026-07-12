import os
import time
import ctypes  # for popup
import threading

REPEAT_INTERVAL = 10  # in seconds (e.g., 3600 = 1 hour)

def remind():
    # Speak using PowerShell
    os.system('powershell -Command "Add-Type –AssemblyName System.Speech;'
              '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;'
              '$speak.Speak(\'Hey ganesh, drink water\')"')

    # Show popup message
    ctypes.windll.user32.MessageBoxW(0, "Hey ganesh, Drink water!", "Reminder", 0x40 | 0x1)

while True:
    remind()
    time.sleep(REPEAT_INTERVAL)
