'''5.	Write a program to add the elements of 2 arrays that are of the same dimension. '''
list1 = [1,2,3,4]
list2 = [4,5,6,7]
res = []
for i in range(len(list1)):
    res.append(list1[i]+list2[i])
print(res)

