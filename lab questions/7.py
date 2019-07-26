#numbers divisible by 9 but not by 5
LB = int(input("enter the number"))
UB = int(input("enter the number"))
for i in range(LB,UB+1):
    if i % 9 == 0 and i % 5 != 0:
        print(i,end = " ")
