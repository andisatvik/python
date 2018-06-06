# Take 2 lists - use a list comprehension to check common numbers and display in a 3rd list

import random

a = random.sample(range(15),7)
print(a)
b = random.sample(range(15),9)
print(b)

cl = [i for i in set(a) if i in b]

print(cl)
