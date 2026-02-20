# break and continue is the statement in python used to skip the iteration and break the iteration
    # 1. continue statement
           #  continue is being used on an itereation to skip the perticular iteration
    # 2. break statement
           # break is being used to an iteration to stop and exit to the loop instantlly

# example of continue
# table of 6 using for loop with 6 X 6 iteration is skiped using continue statement
for i in range(12):
  if (i == 6):
    print("Skip the iteration.")
    continue
  print("6 X", i, "=", 6 * i)
  
# example of break 
# printing 1 to 99 using for loop with break statement which breaks the loop at condition where i == 100 so 100 is not get printed
i = 1
while True:
  print(i)
  i +=1
  if(i == 100):
    break 
