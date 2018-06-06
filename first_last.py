# FIirst and Last of list

import random

a = random.sample(range(23),9)
print(a)

def get_first(list):
    f = list[0]
    return f

def get_last(list):
    l = list[-1]
    return l

lis = []
lis.append(get_first(a))
lis.append(get_last(a))
print(lis)
