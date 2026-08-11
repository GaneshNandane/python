# Raising a custom error

# The salary must be between 2000 and 5000.
# If the salary is outside this range, raise a ValueError.

salary = int(input("Enter salary amount: "))

if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
