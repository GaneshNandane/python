# simple program to demonstrate the use strftime() function

# here it converts it into string according to format you provide 
import time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)
