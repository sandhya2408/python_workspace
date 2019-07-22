import random as rn
generator = rn.randint(1,6)
count = 0
while True:
    num = int(input("enter the input: "))
    if num == generator:
         count += 1
         break
    elif num < generator:
        print(" guessed number is less than actual number")
        count += 1
    else:
        print(" guessed number is less than actual number")
        count += 1
    if count == 3:
        print("better luck next time")
        break