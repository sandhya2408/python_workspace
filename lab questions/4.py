#prime number between range
def prime(n):
    if n < 2:
        return False
    else:
        for i in range (2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

LB = int(input("enter the number"))
UB = int(input("enter the number"))
for i in range (LB,UB+1):
    if prime(i):
        print(i)