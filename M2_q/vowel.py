'''4.	Write a program to accept an input string from the user and determine the vowels in the string and calculate the number of vowels'''
word = input("enter a string")
count = 0
lst = ['a','e','i','o','u','A','E','I','O','U']
print(len(list(filter(lambda x : x in lst, word))))
    
 