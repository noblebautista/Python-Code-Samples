# Program Name: time2.py
# Purpose of a program:
# User inputs current time and hours to wait.
# Then program returns the time user's waiting time ends.
########################################################################################
# Noble Bautista = Editor

str_time = input("What time is it now?") #asks for user input (will be variable str_time)
str_wait_time = input("What is the number of hours to wait?") #asks for user input (will be variable str_wait_time)
time = int(str_time)
wait_time = int(str_wait_time) #defines variables as integers

time_when_start = time + wait_time #formula for time_when_start
print(time_when_start) #prints start time
