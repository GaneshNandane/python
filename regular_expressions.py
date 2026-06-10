# regular expressions
# regular expressions are the pattern that match, search, extract, replace text in strings 
# regex finds a perticular pattern inside a string and matches them with the pattern that we decide what text we want to extract from the string 
# regex can be used to modify text, validate user inputs to a perticular inbox for better data collection and data handling 
# it also can be used in game commands or developer commands to handle games and game modes
# it has strong command on the string data type to manipulate text data 

# here is one example of the username input validator where we specifiying the rules and guidlines to set ingame username to a perticular user or player


import re

def validate_username(username):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{2,15}$"
    
    if re.match(pattern, username):
        return True
    return False

usernames = [
    "hello_23s",
    "_dfgoga_35",
    "2djraj_3204",
    "MaskMan_07",
    "Henr_lol_topplayer07",
    "Red@rabit24"
]

for username in usernames:
    if validate_username(username):
        print(f"{username} <----- valid username")
    else:
        print(f"{username} <----- invalid username")
