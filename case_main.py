# checking the input number provided by the user and sorting that number using match case 
# here we have all posible conditions for the input variable x match x checks them one by one for every case with custom condition provided by the devloper and executes the case blocks that matches the condition
# so that's how number is get sorted on the basis of condition

x=int(input("Enter the value of x:"))
match x:
    case 0:
        print("X is zero")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)
