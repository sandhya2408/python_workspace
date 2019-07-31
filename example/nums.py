import random as rn 

nums = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
allnums = [j for i in nums for j in i]
print(allnums)