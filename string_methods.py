# ---------------------------------------------------------------------------------------------------
# STRINGS IN PYTHON
# ---------------------------------------------------------------------------------------------------
# Strings are immutable in Python.
# This means once a string object is created, its value cannot be changed.
# Any string method that seems to modify a string actually returns a NEW string.
# The original string always remains unchanged in memory.

message = "This is the message to everyone that the beginning is the key to success"

# ---------------------------------------------------------------------------------------------------
# 1. capitalize()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.capitalize()
# This method returns a new string where:
# - The first character of the entire string is converted to uppercase (if it is a letter).
# - All remaining characters are converted to lowercase.
# It does NOT modify the original string.

x = message.capitalize()
print(x)


# ---------------------------------------------------------------------------------------------------
# 2. casefold()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.casefold()
# This method converts the string to lowercase in a more aggressive way than lower().
# It is designed for caseless string comparison across different languages.
# For example, certain special characters in German are handled better with casefold().

x = message.casefold()
print(x)


# ---------------------------------------------------------------------------------------------------
# 3. center()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.center(width, fillchar)
# - width: Total length of the resulting string.
# - fillchar (optional): Character used to fill padding (default is space).
# If width is greater than the string length:
#     Padding is added equally on both sides.
# If width is less than or equal to string length:
#     Original string is returned unchanged.

x = message.center(120, "-")
print(x)


# ---------------------------------------------------------------------------------------------------
# 4. count()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.count(substring, start, end)
# Returns the number of non-overlapping occurrences of substring in the string.
# Optional start and end parameters restrict the search range.
# Returns 0 if substring is not found (does NOT raise error).

x = message.count("the")
print(x)


# ---------------------------------------------------------------------------------------------------
# 5. encode()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.encode(encoding="utf-8", errors="strict")
# Converts the string into bytes using specified encoding.
# Useful when writing text to files or sending data over networks.

x = message.encode("utf-8")
print(x)


# ---------------------------------------------------------------------------------------------------
# 6. endswith()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.endswith(suffix, start, end)
# Returns True if string ends with specified suffix.
# Optional start and end restrict the checking range.
# Returns Boolean only (never raises error).

x = message.endswith("success")
print(x)


# ---------------------------------------------------------------------------------------------------
# 7. expandtabs()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.expandtabs(tabsize=8)
# Replaces tab character (\t) with spaces.
# Tab expansion depends on current column position.
# Default tab size is 8 spaces.

tab_text = "Hello\tWorld"
x = tab_text.expandtabs(4)
print(x)


# ---------------------------------------------------------------------------------------------------
# 8. find()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.find(substring, start, end)
# Returns lowest index of substring.
# If substring is NOT found, returns -1.
# Does NOT raise an exception.

x = message.find("everyone")
print(x)


# ---------------------------------------------------------------------------------------------------
# 9. format()
# ---------------------------------------------------------------------------------------------------
# Syntax: "string {}".format(value)
# Used to insert values into placeholders {}.
# Supports positional and named arguments.

formatted = "The price is {} dollars".format(49)
print(formatted)


# ---------------------------------------------------------------------------------------------------
# 10. format_map()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.format_map(dictionary)
# Similar to format(), but takes a dictionary directly.
# Placeholders must match dictionary keys.

data = {"name": "Shruti", "age": 21}
msg = "Happy birthday {name}, you are now level {age}!"
print(msg.format_map(data))


# ---------------------------------------------------------------------------------------------------
# 11. index()
# ---------------------------------------------------------------------------------------------------
# Syntax: string.index(substring, start, end)
# Same as find(), but:
# If substring is NOT found, it raises ValueError.
# Always use safely when you're sure substring exists.

if "everyone" in message:
    print(message.index("everyone"))


# ---------------------------------------------------------------------------------------------------
# 12. isalnum()
# ---------------------------------------------------------------------------------------------------
# Returns True if all characters are alphanumeric (a-z, A-Z, 0-9).
# No spaces allowed.
# String must not be empty.

print(message.isalnum())


# ---------------------------------------------------------------------------------------------------
# 13. isalpha()
# ---------------------------------------------------------------------------------------------------
# Returns True if all characters are alphabets only.
# Spaces or numbers cause False.

print(message.isalpha())


# ---------------------------------------------------------------------------------------------------
# 14. isascii()
# ---------------------------------------------------------------------------------------------------
# Returns True if all characters are valid ASCII (0-127).
# Never raises error.

print(message.isascii())


# ---------------------------------------------------------------------------------------------------
# 15. isdecimal()
# ---------------------------------------------------------------------------------------------------
# Returns True only if all characters are decimal digits (0-9).
# Very strict numeric check.

print("12345".isdecimal())


# ---------------------------------------------------------------------------------------------------
# 16. isdigit()
# ---------------------------------------------------------------------------------------------------
# Returns True if all characters are digits.
# Allows superscripts and some special digit characters.

print("12345".isdigit())


# ---------------------------------------------------------------------------------------------------
# 17. isidentifier()
# ---------------------------------------------------------------------------------------------------
# Returns True if string is a valid Python identifier.
# Must follow variable naming rules:
# - Cannot start with digit
# - Cannot contain spaces
# - No special characters except underscore

print("variable_name".isidentifier())


# ---------------------------------------------------------------------------------------------------
# 18. islower()
# ---------------------------------------------------------------------------------------------------
# Returns True if:
# - There is at least one alphabet character
# - All alphabet characters are lowercase
# Non-letter characters are ignored.

print(message.lower().islower())


# ---------------------------------------------------------------------------------------------------
# 19. isnumeric()
# ---------------------------------------------------------------------------------------------------
# Returns True if all characters are numeric.
# Includes fractions, Roman numerals, etc.

print("12345".isnumeric())


# ---------------------------------------------------------------------------------------------------
# 20. isprintable()
# ---------------------------------------------------------------------------------------------------
# Returns False if string contains non-printable characters like \n or \t.

print(message.isprintable())


# ---------------------------------------------------------------------------------------------------
# 21. isspace()
# ---------------------------------------------------------------------------------------------------
# Returns True if string contains ONLY whitespace characters.
# Includes space, \n, \t, \r etc.

print("   ".isspace())


# ---------------------------------------------------------------------------------------------------
# 22. istitle()
# ---------------------------------------------------------------------------------------------------
# Returns True if each word starts with uppercase letter
# and remaining letters are lowercase.

print(message.title().istitle())


# ---------------------------------------------------------------------------------------------------
# 23. isupper()
# ---------------------------------------------------------------------------------------------------
# Returns True if:
# - At least one letter exists
# - All letters are uppercase

print(message.upper().isupper())


# ---------------------------------------------------------------------------------------------------
# 24. join()
# ---------------------------------------------------------------------------------------------------
# Syntax: separator.join(iterable)
# Joins elements of iterable into single string.
# Separator is placed between elements.

items = ["oil", "sugar", "peanuts"]
print(", ".join(items))


# ---------------------------------------------------------------------------------------------------
# 25. ljust()
# ---------------------------------------------------------------------------------------------------
# Left justifies string.
# Adds padding to right side to reach total width.

txt = "banana"
print(txt.ljust(15, "*"))


# ---------------------------------------------------------------------------------------------------
# 26. lower()
# ---------------------------------------------------------------------------------------------------
# Converts all uppercase letters to lowercase.

print(message.lower())


# ---------------------------------------------------------------------------------------------------
# 27. lstrip()
# ---------------------------------------------------------------------------------------------------
# Removes characters from left side only.
# Default removes whitespace.

txt = "     banana     "
print(txt.lstrip())


# ---------------------------------------------------------------------------------------------------
# 28. maketrans() + translate()
# ---------------------------------------------------------------------------------------------------
# maketrans() creates translation table.
# translate() applies that mapping to string.

txt = "Hello Sam!"
table = str.maketrans("S", "P")
print(txt.translate(table))


# ---------------------------------------------------------------------------------------------------
# 29. partition()
# ---------------------------------------------------------------------------------------------------
# Splits string into 3 parts:
# (before separator, separator, after separator)
# If separator not found:
# returns (original_string, '', '')

print(message.partition("everyone"))


# ---------------------------------------------------------------------------------------------------
# 30. replace()
# ---------------------------------------------------------------------------------------------------
# Replaces ALL occurrences unless count is specified.
# Returns new string.

print(message.replace("beginning", "start"))


# ---------------------------------------------------------------------------------------------------
# 31. rfind()
# ---------------------------------------------------------------------------------------------------
# Searches from right to left.
# Returns highest index.
# Returns -1 if not found.

print(message.rfind("the"))


# ---------------------------------------------------------------------------------------------------
# 32. rindex()
# ---------------------------------------------------------------------------------------------------
# Same as rfind but raises ValueError if not found.

if "the" in message:
    print(message.rindex("the"))


# ---------------------------------------------------------------------------------------------------
# 33. rjust()
# ---------------------------------------------------------------------------------------------------
# Right justifies string.
# Adds padding to left side.

print(txt.strip().rjust(15, "*"))


# ---------------------------------------------------------------------------------------------------
# 34. rpartition()
# ---------------------------------------------------------------------------------------------------
# Splits at last occurrence of separator.

sentence = "I like bananas and bananas are sweet"
print(sentence.rpartition("bananas"))


# ---------------------------------------------------------------------------------------------------
# 35. rsplit()
# ---------------------------------------------------------------------------------------------------
# Splits from right side.
# maxsplit defines number of splits from right.

print(message.rsplit(" ", 2))


# ---------------------------------------------------------------------------------------------------
# 36. rstrip()
# ---------------------------------------------------------------------------------------------------
# Removes characters from right side only.

msg2 = "hello123"
print(msg2.rstrip("123"))


# ---------------------------------------------------------------------------------------------------
# 37. split()
# ---------------------------------------------------------------------------------------------------
# Splits string into list.
# Default separator is whitespace.

print(message.split())


# ---------------------------------------------------------------------------------------------------
# 38. splitlines()
# ---------------------------------------------------------------------------------------------------
# Splits string at line boundaries.
# keepends=True keeps newline characters.

multi = "Hello\nWorld"
print(multi.splitlines())


# ---------------------------------------------------------------------------------------------------
# 39. startswith()
# ---------------------------------------------------------------------------------------------------
# Returns True if string starts with specified prefix.

print(message.startswith("This"))


# ---------------------------------------------------------------------------------------------------
# 40. strip()
# ---------------------------------------------------------------------------------------------------
# Removes characters from both sides.
# Default removes whitespace.

print("   banana   ".strip())


# ---------------------------------------------------------------------------------------------------
# 41. swapcase()
# ---------------------------------------------------------------------------------------------------
# Converts lowercase to uppercase and vice versa.

print(message.swapcase())


# ---------------------------------------------------------------------------------------------------
# 42. title()
# ---------------------------------------------------------------------------------------------------
# Capitalizes first letter of each word.

print(message.title())


# ---------------------------------------------------------------------------------------------------
# 43. translate()
# ---------------------------------------------------------------------------------------------------
# Dictionary-based translation using ASCII values.

mapping = {83: 80}  # S -> P
print("Hello Sam!".translate(mapping))


# ---------------------------------------------------------------------------------------------------
# 44. upper()
# ---------------------------------------------------------------------------------------------------
# Converts all letters to uppercase.

print(message.upper())


# ---------------------------------------------------------------------------------------------------
# 45. zfill()
# ---------------------------------------------------------------------------------------------------
# Pads zeros on the LEFT to reach total width.
# If string length >= width, returns original string.

print("25".zfill(5))
