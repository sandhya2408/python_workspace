'''1. write a program to accept a number and detrmine whether it is prime'''

num = int(input("enter the number"))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
           is_prime = False
           break
if is_prime:
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
    
num = int(input("enter the number"))

num = int(input("enter the number"))

num = int(input("enter the number"))