# this is the simple version of kon banega karodpati
# here it asks us ten questions after every question the price increased 

questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", 4],
    ["Which company developed Python?", "Google", "Microsoft", "Python Software Foundation", "Meta", 3],
    ["Who is the founder of Microsoft?", "Steve Jobs", "Bill Gates", "Elon Musk", "Mark Zuckerberg", 2],
    ["Which data structure stores unique elements?", "List", "Tuple", "Set", "Dictionary", 3],
    ["Which keyword is used to define a function in Python?", "func", "define", "def", "function", 3],
    ["Which operator is used for exponentiation in Python?", "^", "**", "*", "%", 2],
    ["Which company developed the C language?", "Microsoft", "Apple", "Bell Labs", "Google", 3],
    ["Which symbol is used for comments in Python?", "//", "/*", "#", "--", 3],
    ["Which loop is used when the number of iterations is known?", "while", "for", "do-while", "repeat", 2],
    ["Which keyword is used to create a class in Python?", "class", "Class", "struct", "object", 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0

for i in range(len(questions)):
    question = questions[i]

    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"1. {question[1]}          2. {question[2]}")
    print(f"3. {question[3]}          4. {question[4]}")

    reply = int(input("Enter your answer (1-4) or 0 to quit: "))

    if reply == 0:
        if i == 0:
            money = 0
        else:
            money = levels[i - 1]
        break

    if reply == question[-1]:
        print(f"Correct Answer! You have won Rs. {levels[i]}")

        # Safe prize levels
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        else:
            money = levels[i]
    else:
        print("Wrong Answer!")
        break

print(f"\nYou take home Rs. {money}")
