# function with arguments 
# we can give a fuction a argument and fuction returns that argument inside the fuction and perform some operatins on it and gives us output if we use this fuction 

# example of fuction argument with average function which converts averge of the numbers

def average(*numbers):
  total = 0
  for i in numbers:
    total += i
  return total / len(numbers)

num = input("Enter numbers: ")
numbers = list(map(int, num.split()))
result = average(*numbers)
print(f"Average is:",result)
