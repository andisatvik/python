# Reverse a string

s = input("Enter the sentence to be reversed: ")

def rev_str(string):
    rev_list = string.split(" ")[::-1]
    rev = " ".join(rev_list)
    print(rev)

rev_str(s)
