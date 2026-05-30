import time

time_india = time.localtime()
formated_time = time.strftime("%H:%M:%S", time_india)
print(formated_time)

time.sleep(5)
time_india = time.localtime()
formated_time1 = time.strftime("%H:%M:%S", time_india)
print(formated_time1)
