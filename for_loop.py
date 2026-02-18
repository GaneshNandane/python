# for loops are used to iterate over a string, list, set, dictionary, tuple we can access every element inside any data type using loops
# for loop is mainly used as an iterator


fruitslist = ["Banana", "Apple", "Orange", "Grapes", "Papaya"]
for i in fruitslist:
  print(i)

name = "Ganesh Nandane"
for x in name:
  print(x)


# we can run for loop inside a for loop 

listofworks = ["writing", "reading"]
listofbooks = ["textbook", "workbook", "dictionary", "diarry"]
for a in listofworks:
  for b in listofbooks:
    print(a, b)

# we can use else with for loops 

for c in range(5):
  print(c)
else:
  print("work is done.")
