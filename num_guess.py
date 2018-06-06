# Guess the number

import random

num = random.randint(1,9)
count = 0

while(1):
    guess = int(input("Enter your guess: "))

    if guess < num:
        print("Too low")
        count+=1

    elif guess == num:
        print("Good guess")
        count+=1
        break
    
    else:
        print("Too High")
        count+=1

print("You took "+str(count)+" tries to get there!") 
