'''7.	Write a program to find the sum of squares of only the even numbers in the given list. '''
list = [1,2,3,4,5,6,7,8,9]
sum = 0
for num in list:
    if num % 2 == 0:
        s = num * num
        sum = sum + s
print(sum)