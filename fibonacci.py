# Use fn, take user input for length of fibonacci and then print

n = int(input("Enter the desired length of fibonacci: "))

def get_fib(num):
    i=1
    j=1
    iter=0
    fib = []
    while(iter < num):
        fib.append(j)
        temp = i+j
        j=i
        i=temp
        iter+=1
    return(fib)

res = get_fib(n)
print(res)
