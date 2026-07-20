# Taking the year as input from the user
year = int(input("Enter a year: "))

# First check if the year is divisible by 4
if year % 4 == 0:

    # If it is also divisible by 100, we need another check
    if year % 100 == 0:

        # A year divisible by both 100 and 400 is a leap year
        if year % 400 == 0:
            print("Year is a leap year")
        else:
            print("Year is not a leap year")

    # If the year is divisible by 4 but not by 100,
    # it is a leap year.
    else:
        print("Year is a leap year")

# If the year is not divisible by 4,
# it is not a leap year.
else:
    print("Year is not a leap year")
