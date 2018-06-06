# Print all divisors for entered number

num = int(input("Please enter number: "))

num_list = range(1,num+1)
divisors = []

for i in num_list:
    if(num%i == 0):
        divisors.append(i)

print("Divisors for "+str(num)+" are: "+str(divisors))
