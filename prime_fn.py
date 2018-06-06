# Using function to check for primality of a number

def find_divisors(num):
    num_list = range(1,num+1)
    divisors = []

    for i in num_list:
        if(num%i == 0):
            divisors.append(i)

    return divisors

entry = int(input("Please enter number: "))
div_list = find_divisors(entry)

if(len(div_list) == 2):
    print("Prime")
else:
    print("Not a Prime")
