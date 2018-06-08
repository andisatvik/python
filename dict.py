
birthdays = {
        "Albert Einstein": "12-Jun-1660",
        "Benjamin Franklin": "3-Jul-1171",
        "Ada Lovelace": "12-Jan-1994"
        }

print("Welcome to the birthday dictionary. We know the birthdays of:\n"+str(birthdays.keys()))

name = input("Whose brithday do you want to know? ")

print(name+"'s birthday falls on: "+birthdays[name])
