#biggest of 3 numbers
def biggest(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))
res = biggest(num1,num2,num3)
print(f"{res} is the largest ")