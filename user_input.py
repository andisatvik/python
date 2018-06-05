# User enters name and age ...

import datetime

curr_year = datetime.date.today().year
name = input("Please enter name : ")
age = input("Please enter age : ")

#print(curr_year - int(age) + 100)

print(name,", Your age will be 100 in the year: ",(curr_year - int(age) +100))
