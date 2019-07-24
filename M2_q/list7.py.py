'''6.	Write a program to find the sum of the given elements of the list. (Hint: Use reduce method.) '''
from functools import reduce
list = [1,2,3,4,5,6,7,8,9]
res = reduce(lambda a,b:a+b,lst)
print(res)