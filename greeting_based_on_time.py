# this is the simple example of the time module which simply displays the current time and greet the person with the good afternoon or good morning or good evening on the basis of time  

import time
t=int(time.strftime('%H'))
Time = time.strftime('%H:%M:%S')
print(Time)
if t<12:
    print("Good morning sir")
elif t<17:
    print("Good afternoon sir")
else:
    print("Good evening sir")
