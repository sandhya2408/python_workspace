#sumof digits till single digit
sum = 0
count = 0
def find_sum(num):
    sum = 0
    while num > 0 or sum > 9:
        if num == 0:
            num = sum 
            sum = 0
        sum += num % 10
        num = num // 10
    return sum
num = int(input("enter the number:"))
res = find_sum(num)
print(res)


'''or 
tnum = num = int(input("enter a number"))
while num > 9:
    sum = (num % 10 +num //10)
    num = sum
    print(f"sum of digits of {tnum} is = {num}")
    '''