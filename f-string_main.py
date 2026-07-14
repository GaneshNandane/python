# Comparing the format() function with f-strings

# Using the format() function
# The placeholders {1} and {0} refer to the second and first arguments
# passed to the format() method, respectively.
letter = "Hey, my name is {1} and I am from {0}"

country = "India"
name = "Harry"

# Here, country becomes {0} and name becomes {1}
print(letter.format(country, name))

# Using an f-string
# Variables are inserted directly into the string without using format().
print(f"Hey, my name is {name} and I am from {country}")

# To print curly braces literally, use double curly braces {{ }}
print(f"We use f-strings like this: Hey, my name is {{name}} and I am from {{country}}")

# Formatting a floating-point number
# :.2f displays the number with exactly 2 digits after the decimal point.
price = 49.999999
txt = f"For only {price:.2f} dollars!"
print(txt)

# f-strings can also evaluate expressions directly.
print(f"{2 * 30}")

# The result of an f-string is always a string.
print(type(f"{2 * 30}"))
