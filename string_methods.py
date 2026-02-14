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
  # syntax
    # string.encode(encoding="utf-8", errors="strict")
# converts a string (text) into bytes using a specific encoding format
x = message.encode()
print(x)

# 6. endswith()
  # syntax
    # string.endswith(suffix, start, end)
# finds if the specific text ends with a specific symbol or a specific text with a range with two parameters of start and end index
x = message.endswith(".")
print(x)

# 7. expandtabs()
  # syntax
    # string.expandtabs(tabsize)
# here expantabs method does is to expand the tab space to cirtain conditions with the default being 8 spaces that means if our text has two characters then the tabsize of 6 gets added that is 8-2 = 6 where two is the actual text size and their is a one problem what if our text is larger that 8 text characters then their comes the one anoter case that the next tab space is the multiple of 8 means that 16- our text size and outputed results number tab gets included it has custom tab size also if we do not like default 8 space tab we can set to our need
x =  message.expandtabs(2)
print(x)

# 8. find()
  # syntax
    # string.find(substring, start, end)
# find the first occurence of the text that we provide to the method it returns the index of the first occurence and it has two parameters start and end means that if we want we can find text in specific indexing or we can say area of our field
x = message.find("welcome")
print(x)

# 9. format()
  # syntax
   # 1.  "string with {} placeholders".format(value1, value2)
   # 2. "string with {name}".format(name=value)
# it uses the curlly braces to store any value that we provid to the into format method with first come first surv basis so we need to know where the value need which value it is old style it has been replaced by f-strings now
# it also has a equal to symbol to works as format_map except : we have = here it also works as the f-strings
print(message.format(price = 49))

# 10. format_map()
  # syntax
    # string.format_map(mapping)
# it is similar to the format but it takes dictionary elements with key value pairs to be able to place at a placeholder and it works exactlly as f-strings
name_dictionary = {"name" : "Shruti", "age" : 21}
message2 = "Happy birthday {name} you are now on level {age}!"
print(message2.format_map(name_dictionary))

# 11. index()
  # syntax
    # string.index(substring, start, end)
# it is exactlly similar to the find method instead of the program termination if the value is not found here we have value error that the value is not found
x = message.index("welcome")
print(x)

# 12. isalnum()
  # syntaxx
    # string.isalnum()
# it checks if the value in the string are all alphabets and numbers it shoud be not empty string then and then it gives the output to the console true unless it gives false output
x = message.isalnum()
print(x)

# 13. isalpha()
  # syntax
    # string.isalpha()
# it checks if the string has contains alphabets only if it contains any element except alphabets including spaces it gives flase error and it must not be an empty string 
x = message.isalpha()
print(x)

# 14. isascii()
  # syntax
    # string.isascii()
# it checks if the text contains all the ascii characters if not then it gives error to the console saying false
x = message.isascii()
print(x)

# 15. isdecimal()
  # syntax
    # string.isdecimal()
# it checks if the all characters in the string are numbers if not then it gives error saying false
x = message.isdecimal()
print(x)

# 16. isdigit() 
  # syntax
    # string.isdigit()
# it is similar to the isdecimal but it is not much strikter than isdecimal it allows special digit characters like superscripts it prints true if it satisfyes each condition unless it prints false to the console
x = message.isdigit()
print(x)

# 17. isidentifier()
  # syntax
    # string.isidentifier()
# so basiclly it checks and follwos the rule of the varialbe creation in an string if it follows all rules then and then it gives the true output else it gives false output
x = message.isidentifier()
print(x)

# 18. islower()
  # syntax
    # string.islower()
# it works only on the letters with lowercase value if any value in the string are lowercase then the console gives false output for empty strings this gives error or false value 
x = message.islower()
print(x)

# 19. isnumeric()
  # syntax
    # string.isnumeric()
# it checks if the all the value of the strings are digits fractions or roman numerals if it's not then it gives error saying false
x = message.isnumeric()
print(x)

# 20. isprintable()
  # syntax
    # string.isprintable()
# it checks whether the values of the string are all printable means that if it contains special characters which is know to compiler as the \n, \t etc then it gives error saying false
x = message.isprintable()
print(x)

# 21. isspace()
  # syntax
    # string.isspace()
# it strictlly checks if the string contains only and only white spaces not that it also contains special charter which is known to compiler that creates white spaces like \n, \t, \r etc then it gives true unless it gives false if all conditions are not get satisfied
x = message.isspace()
print(x)

# 22. istitle()
  # syntax
    # string.istitle()
# it checks if the all word in the strings are starts with uppercase letters if does not satisfyies this condition then it gives error to the console saying false
x = message.istitle()
print(x)

# 23. isupper() 
  # syntax
    # string.isupper()
# it checks if all the letters in the strings are uppercase or not if not then the compiler prints the error saying false
x = message.isupper()
print(x)

# 24. join()
  # syntax
    # separator.join(iterable)
# it joins the multiple collection of strings like list tuple or any string collection by a seperator to form a single individual string 
ration_list = ["oil", "sugar", "peanuts", "soyachunks"]
x = ",".join(ration_list)
print(x)

# 25. ljust()
  # syntax
    # string.ljust(width, fillchar)
# it specified the left justify means that the string can be justified to the left or in simple words we can add any characters to the left of the string this method has two parameters width and fillchar where width is the total length of the string after the method has been applied and fillchar is the parameter where we provide the symbol or any value that we want to add followed by the width that specified that how many times this symbol repeats to the left here is one condition occur that if the width of the string is less than the length of the string then the actual string gets printed  
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# 26. lower()
  # syntax
    # string.lower()
# it converts all uppercase letter in a string to lowercase letter numbers and special symbols are not get affected
x = message.lower()
print(x)

# 27. lstrip()
  # syntax
    # string.lstrip([chars])

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
