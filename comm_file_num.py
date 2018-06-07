
with open("primenumbers.txt","r") as file_1:
    prime = list(file_1.read())

with open("happynumbers.txt","r") as file_2:
    happy = list(file_2.read())

new_list = [a for a in prime if a in happy and a!='\n']

print(new_list)
