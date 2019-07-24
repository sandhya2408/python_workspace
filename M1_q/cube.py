'''	Write a program to accept a number “n” from the user; then display the sum of the following series:
1/23 + 1/33 + 1/43 + …… + 1/n3'''
sum = 0
num = int(input("enter the number"))
for i in range(1,num+1):
    sum = sum + 1/i**3
print(f"sum of series is {sum}")