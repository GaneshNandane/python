import pyttsx3

# initializing the ttx enginge (Text To Speech)
engine = pyttsx3.init()

# pass the text that should be converted into speech 
engine.say("""3. Problem Characteristics
Short Notes:
Important aspects:

Decomposability: Can the problem be broken into sub-problems?

Solution Type: State or path.

Reversibility: Can actions be undone?

Predictability: Is the problem space predictable?

Knowledge Role: Is domain knowledge required?

Interactivity: Does solving require interaction?

Sample Answer (6 Marks):
Problem characteristics help us understand and classify AI problems. A problem can be decomposable into sub-problems or may need a path to a goal rather than a final state. Some problems allow undoing steps (reversible), while others require comparison of all solutions to find the best. Predictability of the environment and the role of knowledge (like domain-specific rules) are also considered. Interactive problems require user involvement. Analyzing these helps in selecting the best AI technique for solving a problem efficiently.

""")

# conveting the text into speech and wait until the speeking is done 
engine.runAndWait()
