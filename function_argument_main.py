# Function Arguments in Python

# 1. Required (Positional) Arguments
# Both 'a' and 'b' must be provided when calling the function.
def add(a, b):
    print("Addition:", a + b)

# 2. Default Arguments
# 'c' has a default value of 1.
# If no value is passed for 'c', Python uses the default value.
def average(a, b, c=1):
    avg = (a + b + c) / 3
    print("Average:", avg)

# 3. Variable-Length Positional Arguments (*args)
# Accepts any number of positional arguments and stores them in a tuple.
def calculate_average(*numbers):
    print("\nType of numbers:", type(numbers))

    total = 0
    for num in numbers:
        total += num

    avg = total / len(numbers)
    print("Numbers:", numbers)
    print("Average:", avg)

    return avg

# 4. Variable-Length Keyword Arguments (**kwargs)
# Accepts any number of keyword arguments and stores them in a dictionary.
def person_details(**details):
    print("\nType of details:", type(details))

    print("First Name :", details["fname"])
    print("Middle Name:", details["mname"])
    print("Last Name  :", details["lname"])

# Function Calls

print("1. Required Arguments")
add(10, 20)

print("\n2. Default Arguments")
average(4, 6)          # Uses default value c = 1
average(4, 6, 8)       # Uses c = 8

print("\n3. Variable-Length Positional Arguments (*args)")
result = calculate_average(5, 6, 7, 1)
print("Returned Average:", result)

print("\n4. Variable-Length Keyword Arguments (**kwargs)")
person_details(
    fname="James",
    mname="Buchanan",
    lname="Barnes"
)
