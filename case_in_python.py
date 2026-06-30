# here is the implementation of the match case statements 
# here we have all posible conditions for the variable x match x checks them one by one for every case with custom condition provided by the devloper and executes the case blocks that matches the condition 

x=4
match x:
    case 0:
        print("X is zero")
    case 4 if x%2==0:
        print("X%2==0 and case is 4")
    case _ if x < 10:
        print("X is <10")
    case _:
        print(x)
