#sum of elements in the list
def sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
lst = [2,5,4,1,3]
res = sum(lst)
print(f"the sum of elements in the list {lst} is {res}")