# simple program to demonstrate the use of while loop 

# you need to write same lines of code for five times
i=int(input("Enter the number: "))
print(i)

# you can define this lines in while loop for multiple execution while avoiding to write these lines again and again for five times 
while(i<=5):
    i=int(input("Enter the number: "))
    print(i)
print("Done with the loop")
