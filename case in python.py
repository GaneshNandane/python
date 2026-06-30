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