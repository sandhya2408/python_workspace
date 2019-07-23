'''4.	Write a program to accept an input string from the user and determine the vowels in the string and calculate the number of vowels'''
word = input("enter a string")
count = 0
list = []
for letter in word: 
    if letter == 'A' or letter == 'E' or letter == 'I' or  letter == 'O' or letter == 'U' or letter == 'a' or letter =='e' or letter == 'i' or letter =='o' or letter == 'u':
        list.append(letter)
        count += 1
print(list)
print(count)
    
 