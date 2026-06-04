# Walrus Operator
    # The main advantage of the walrus operator is that it can make
    # code more concise and avoid repeating the same expression.

numbers = [5, 10, 15, 20]

# Both the ordinary method and the walrus operator method
# produce the same output.

# Ordinary method
count = len(numbers)

if count > 3:
    print(f"There are {count} numbers in the list.")

# Walrus operator method
    # The walrus operator (:=) allows us to assign a value to a variable
    # as part of an expression and use it in the same line.

if (count := len(numbers)) > 3:
    print(f"There are {count} numbers in the list.")
