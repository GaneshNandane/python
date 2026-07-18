# here in this program we are checking if the number provided by the user is negative zero or positive 

num = int(input("Enter any number: "))

# condition for negative  
if(num<0):
    print("Number is negative.")
# condition for zero  
elif(num==0):
    print("Number is zero.")
# condition for positive  
else:
    print("Number is positive.")
