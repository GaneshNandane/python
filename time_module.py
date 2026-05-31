# time module
    # time module in python works with the time related functions for working with time, dates, delays and timestamps 
    # this is the below example of time module
# here we are providing real time local time and printing on to the console with some delay using sleep function 
import time

time_india = time.localtime()
formated_time = time.strftime("%H:%M:%S", time_india)
print(formated_time)

time.sleep(5)
time_india = time.localtime()
formated_time1 = time.strftime("%H:%M:%S", time_india)
print(formated_time1)

# used to print current date and time on to the console in formated way 
print(time.ctime())

# this is the way to print year, month, and day individually on to the console 
print(t.tm_year)
print(t.tm_mon)
print(t.tm_mday)
