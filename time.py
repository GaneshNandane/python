import datetime
from datetime import datetime

obj =  datetime.now()
print("current Time is: ", obj)

Day = "Today"
name = input("Enter your name:")
print(f"{Day} is a {name}'s birthday")
today = datetime.datetime.today()
print(f"Today's Date is {today:%d %B, %Y}")