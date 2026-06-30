# printing the table of five using the loop with using a continue to skip an iteration so that the value of 5 X 10 is skiped and not printed instead it prints skip the iteration 

for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)

# printing every iteration of the condition with every iteration being added until the condition becomes true and then break keyword breaks the infinite loop that are continiously being called for each iteration 
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
