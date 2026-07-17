import time

# Get the current time in HH:MM:SS format
t = time.strftime('%H:%M:%S')

# Get the current hour (00–23) and convert it to an integer
hour = int(time.strftime('%H'))

# Print the current time
print("Current Time:", t)

# Check if the current hour is between 12:00 AM and 11:59 AM
if hour >= 0 and hour < 12:
    print("Good Morning sir!")

# Check if the current hour is between 12:00 PM and 4:59 PM
elif hour >= 12 and hour < 17:
    print("Good Afternoon sir!")

# Check if the current hour is between 5:00 PM and 8:59 PM
elif hour >= 17 and hour < 21:
    print("Good Evening sir!")

# If none of the above conditions are true, the time is between
# 9:00 PM and 11:59 PM, so print a good night greeting
else:
    print("Good Night sir!")
