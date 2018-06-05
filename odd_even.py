# Find out even-odd numbers

num = int(input("Enter number: "))
div = int(input("Enter divisor: "))

if (num % 2 == 0):
    print(str(num)+" is Even")
    if(num%4==0):
        print(str(num)+" is divisible by 4")
else: print(str(num)+" is Odd")

if(num%div == 0):
    print(str(num)+" is divisible by "+str(div))
else:
    print(str(num)+" is not divisble by "+str(div))
