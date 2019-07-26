#count of prime digits
num =  int(input("enter a number"))
count = 0
while num != 0:
    rem = num % 10
    if rem in [2,3,5,7]:
        count += 1
    num //= 10
print("count is ",count)
