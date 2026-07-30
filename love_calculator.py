# Python Tkinter GUI-based Love Calculator

# Import everything from the tkinter module
from tkinter import *

# Import the random module to generate a random love percentage
import random

# ---------------------------------------------------------
# Create the main application window
# ---------------------------------------------------------
root = Tk()

# Set the window size (Width x Height)
root.geometry("400x240")

# Set the title of the window
root.title("Love Calculator")

# ---------------------------------------------------------
# Function to calculate a random love percentage
# ---------------------------------------------------------
def calculate_love():
    # String containing digits from 0 to 9
    digits = "0123456789"

    # Generate two random unique digits
    percentage = "".join(random.sample(digits, 2))

    # Display the generated percentage on the result label
    result.config(
        text=f"Love Percentage between both of You: {percentage}%"
    )

# ---------------------------------------------------------
# Heading
# ---------------------------------------------------------
heading = Label(
    root,
    text="Love Calculator - How much is he/she into you?",
    font=("Arial", 12, "bold")
)
heading.pack(pady=10)

# ---------------------------------------------------------
# Input for the first person's name
# ---------------------------------------------------------
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()

# Text box to enter your name
name1 = Entry(root, borderwidth=5)
name1.pack()

# ---------------------------------------------------------
# Input for the partner's name
# ---------------------------------------------------------
slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()

# Text box to enter your partner's name
name2 = Entry(root, borderwidth=5)
name2.pack()

# ---------------------------------------------------------
# Button to calculate love percentage
# ---------------------------------------------------------
bt = Button(
    root,
    text="Calculate",
    width=10,
    command=calculate_love
)
bt.pack(pady=10)

# ---------------------------------------------------------
# Label to display the result
# ---------------------------------------------------------
result = Label(
    root,
    text="Love Percentage between both of You:"
)
result.pack()

# ---------------------------------------------------------
# Start the Tkinter event loop
# This keeps the window open and waits for user actions.
# ---------------------------------------------------------
root.mainloop()
