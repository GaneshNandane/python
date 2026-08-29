# Simple program to display the current date and wish someone a birthday

# Import the datetime module
import datetime

# Get the current date and time
obj = datetime.datetime.now()
print("Current Time is:", obj)

# Store the word "Today"
Day = "Today"

# Ask the user to enter their name
name = input("Enter your name: ")

# Display a birthday message
print(f"{Day} is {name}'s birthday")
print(f"Happy Birthday {name}")

# Get today's date
today = datetime.datetime.today()

# Display today's date in Day Month, Year format
print(f"Today's Date is {today:%d %B, %Y}")
