# User enters name and age ...

import datetime

curr_year = datetime.date.today().year
name = input("Please enter name : ")
age = input("Please enter age : ")
num = int(input("How many number of times do you want the message to be displayed ?"))

#print(curr_year - int(age) + 100)

print(num*(name + ", Your age will be 100 in the year: " + str(curr_year - int(age) +100)+"\n"))
