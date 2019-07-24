'''2.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1 + 1/2 + 1/3 + ……. + 1/n'''
sum = 0
num = int(input("enter the number"))
for i in range(1,num+1):
    sum = sum + 1/i
print(f"sum of series is {sum}")