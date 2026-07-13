import win32com.client
names =["stupidprogramm1", "Aayushgarg15", "yonik", "Niteshupadyay2", "Rameshkumar69"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")
for name in names:
    speaker.speak(f"shoutout to {name}.")