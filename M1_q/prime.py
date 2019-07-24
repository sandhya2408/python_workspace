'''Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers.'''
def prime(n):
    if n < 2:
        return False
    else:
        for i in range (2,n//2+1):
            if n % 2 == 0:
                return False
        return True

m = int(input("enter the number"))
n = int(input("enter the number"))
for i in range (m,n+1):
    if prime(i):
        print(i)
        


