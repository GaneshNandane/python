# python f strings are used for the dynamic workflow of the strings that we can use variable fumctions constants in the string 
import datetime

Day = "Today"
name = input("Enter your name:")
print(f"{Day} is a {name}'s birthday")
today = datetime.datetime.today()
print(f" Today's Date is {today:%d %B, %Y}")
