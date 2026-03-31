# is and == both are two different things in python it can give same results in some exceptional cases 
    # 1.'is'
      # 'is' is checks wheter they are same objects or not so 'is' cheks that and gives us ouptut in boolean form 

    # 2. '=='
      # '==' checks wether the value is same in both the variables or not on the basis of that it gives us boolean output

a = 1000
b = 1000

print(a == b)        # this always gives us output True because both the values are same in both the variables 
print(a is b)        # this gives us output True or False based on your compilers optimization because the int data type is immutable so sometimes it might allocate same memeory address or totally different sometime 

a1 = [1, 2, 3, 5]
b1 = [1, 2, 3, 5]

print(a1 == b1)      # this always gives us output True because both the values are same in both the variables 
print(a1 is b1)      # this always gives us output False because lists are mutable and it always allocates the memory address different for both the vaiables 

# 'is' can be also used to check identity which has same address or identity 
value = None
if value is None:
    print("No value")
