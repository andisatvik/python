# Extract common elements from 2 lists

#importing random to create random lists of a fixed length

import random


a = random.sample(range(54),6)
b = random.sample(range(54),9)
print("a = "+str(a)+"\nb = "+str(b))
c = []

for x in b:
    if (x in a and x in b):
        c.append(x)

print(c)
