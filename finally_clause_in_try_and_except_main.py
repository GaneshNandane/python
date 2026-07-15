# defining the list of numbers and taking an user input for checking if the relative index has a value if the index is out of range then prints exception if not then prints try block 
# and then prints finally block after execution of program whether whichever block is executed 

def func1():
    try:
        l=[1, 5, 6, 7]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am  always executed")
        # print("I am always executed")
x=func1()
print(x)
