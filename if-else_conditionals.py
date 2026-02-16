# if else conditionals are used to execute a certain block of code based upon a condition 

# simple if else conditionals statements 
# consider one example where we need to filter people that can vote so we give a condition in the if condition that people having age>18 are eligible to vote
age = int(input("Enter your age: "))
if(age>18):
  print(f"your age is {age} and you can vote.")
else:
  print(f"your age is {age} and you can not vote.")

# if else elif conditionals statements
# checking if the number entered by the user is positive or negative or zero

number = int(input("Enter the number: "))
if(number<0):
  print("number is negative.")
elif(number == 0):
  print("number is zero")
elif(number == 1000):
  print("number is special.")
else:
  print("number is positive")

# nested if else elif conditionals statements
# price filter in an electronic shop
price = int(input("Enter the product price: "))
if(price > 10000):
  print("Do not buy.")
elif(price < 10000):
  print("You can buy.")
  if(price < 100):
    print("But the product quality might be low.")
  elif(price < 4000):
    print("You can buy limmited products.")
else:
  print("You can buy lots of products.")
