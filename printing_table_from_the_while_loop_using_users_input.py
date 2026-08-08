# printing a multiplication table using a while loop

# taking input from the user
n = int(input("Enter the number for which you want to calculate table for it: "))

# defining a counter starting from 1
i = 1

# giving a condition to the loop
while(i < 11):
    # printing each value
    print(f"{n} X {i} = {n*i}")

    # incrementing the counter
    i += 1
