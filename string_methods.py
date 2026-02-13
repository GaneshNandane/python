# strings are imutable means that the strings are not get changed after creation of the strings

message = "This is the message to everyone that the begining is the key to success"

# strings have different methods to manipulate them and use them viselly

# 1. capitalize()
# first letter of the whole string gets capitalize
x = message.capitalize()
print (x)

# 2. casefold()
# converts string to the lowercase aggressively means that it works in different languages 
x = message.casefold()
print(x)

# 3. center()
  # syntax
    # string.center(width, fillchar)
# used to center the string with the different parameters of width and fillchar note that the width is get substacted from the actual length of the string and then the output get distributed into two parts and both gets added to left and right
x = message.center(20)
print(x)

# 4. count()
  # syntax
    # string.count(substring, start, end)
# returns the number of times a similar text gets appear in the string with parameters of start and end where start means that the it starts from this index same as the end where end index gets specified it finds  till that specified index
x = message.count("apple")
print(x)

# 5. encode()
  # string.encode(encoding="utf-8", errors="strict")
    # converts a string (text) into bytes using a specific encoding format
x = message.encode()
print(x)

# 6. endswith()
  # string.endswith(suffix, start, end)
    # finds if the specific text ends with a specific symbol or a specific text with a range with two parameters of start and end index
x = message.endswith(".")
print(x)

# 7. expandtabs()
  # string.expandtabs(tabsize)
# here expantabs method does is to expand the tab space to cirtain conditions with the default being 8 spaces that means if our text has two characters then the tabsize of 6 gets added that is 8-2 = 6 where two is the actual text size and their is a one problem what if our text is larger that 8 text characters then their comes the one anoter case that the next tab space is the multiple of 8 means that 16- our text size and outputed results number tab gets included it has custom tab size also if we do not like default 8 space tab we can set to our need
x =  message.expandtabs(2)
print(x)

# 8. find()
  # string.find(substring, start, end)
    # find the first occurence of the text that we provide to the method it returns the index of the first occurence and it has two parameters start and end means that if we want we can find text in specific indexing or we can say area of our field
x = message.find("welcome")
print(x)

# 9. format()
# it uses the curlly braces to store any value that we provid to the into format method with first come first surv basis so we need to know where the value need which value it is old style it has been replaced by f-strings now
print(message.format(price = 49))

# 10. format_map()

name_dictionary = {"name" : "Jane", "age" : 36}
message2 = "Happy birthday {name} you are now on level {age}!"
print(message2.format_map(name_dictionary))

# 11. index()
x = message.index("welcome")
print(x)

# 12. isalnum()
x = message.isalnum()
print(x)

# 13. isalpha()
x = message.isalpha()
print(x)

# 14. isascii()
x = message.isascii()
print(x)

# 15. isdecimal()
x = message.isdecimal()
print(x)

# 16. isdigit() 
x = message.isdigit()
print(x)

# 17. isidentifier()
x = message.isidentifier()
print(x)

# 18. islower()
x = message.islower()
print(x)

# 19. isnumeric()
x = message.isnumeric()
print(x)

# 20. isprintable()
x = message.isprintable()
print(x)

# 21. isspace()
x = message.isspace()
print(x)

# 22. istitle()
x = message.istitle()
print(x)

# 23. isupper() 
x = message.isupper()
print(x)

# 24. join()
x = "#".join(myTuple)
print(x)

# 25. ljust()
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# 26. lower()
x = message.lower()
print(x)

# 27. lstrip()
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

# 28. maketrans()
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

# 29. partition()
x = message.partition("bananas")
print(x)

# 30. replace()
x = message.replace("bananas", "apples")
print(x)

# 31. rfind()
x = message.rfind("casa")
print(x)

# 32. rindex()
x = message.rindex("casa")
print(x)

# 33. rjust()
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

# 34. rpartition()
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

# 35. rsplit()
x = message.rsplit(", ")
print(x)

# 36. rstrip()
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

# 37. split()
x = message.split()
print(x)

# 38. splitlines()
x = message.splitlines()
print(x)

# 39. startswith()
x = message.startswith("Hello")
print(x)

# 40. strip()
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

# 41. swapcase()
x = message.swapcase()
print(x)

# 42. title()
x = message.title()
print(x)

# 43. translate()
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# 44. upper()
x = message.upper()
print(x)

# 45. zfill()
x = message.zfill(10)
print(x)
