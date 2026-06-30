# Printing odd numbers from 1 to 99 using the range() function. After printing each number, the message "Mississippi" is displayed. The break statement is never executed because the value 50 is not included in the range of odd numbers.

for i in range(1,101,2):
    print(i, end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
