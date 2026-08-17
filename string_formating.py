# Define a string containing a placeholder for a price
# The .2f format specifier displays the price as a floating-point number
# with exactly two digits after the decimal point
txt = "For only {price:.2f} dollars!"

# Format the string by replacing the {price} placeholder with the value 49
print(txt.format(price=49))
