# this is the simple example of program to find addition of first n natural numbers 

# taking input n 
n = int(input("Enter a number: "))

# defining the value of i 
i = 1

# defining the value of sum 
sum = 0

# giving condition for every value of n, n should be greater or equal to i 
while(i<=n):
    # adding the value of sum to i for every iteration
    sum += i

    # increamenting the value of i for every iteration
    i += 1

# printing the final value of sum
print(sum)
