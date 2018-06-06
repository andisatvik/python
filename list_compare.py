# Bunch of numerical compare operations on a list

l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Find and print all numbers in list less than 5

print("Elelments less than 5 are:")
for n in l:
    if n<5:
        print(n)

# New list with elem < 5

nl = []

for x in l:
        if x<5:
            nl.append(x)
print("The new list is:"+str(nl))


# Writing in one line

for o in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]: 
    if o<5: print(o)

print("One Line Solution" + str([o for o in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if o>13]))
