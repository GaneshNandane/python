# while loop is used where value must be print at onece 

# for loop
i = 1
while(i < 6):
  print(i)
  i += 1

# for loop with break statement
j = 1
while(j < 6):
  print(j)
  if (j == 3):
   break
  j += 1

# for loop with else statement
l = 1
while(l < 6):
  print(l)
  l += 1
else:
  print("l is no longer less than 6")

# for loop with continue statement
k = 0
while(k < 6):
  k += 1
  if (k == 3):
    continue 
  print(k)
