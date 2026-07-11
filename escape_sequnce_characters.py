# Inserting a single quote (') inside a string
string = 'Hi! \'man'
print("By using \\' :", string)

# Inserting a double quote (") inside a string
string = "Hi!\"man"
print('By using \\" :', string)

# Using the newline escape sequence (\n)
string = "Hi\nman"
print("By using \\n:")
print(string)

# Using the tab escape sequence (\t)
string = "Hi!\tman"
print("By using \\t:", string)

# Using the carriage return escape sequence (\r)
string = "Hi!\rman"
print("By using \\r:", string)

# Using the backspace escape sequence (\b)
string = "Hi!\bman"
print("By using \\b:", string)

# Using octal escape sequences (\ooo)
string = "\123\101\124"      # Valid octal values
print("By using octal escapes:", string)

# Using hexadecimal escape sequences (\xhh)
string = "\x54\x34"
print("By using hexadecimal escapes:", string)
