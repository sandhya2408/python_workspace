def binarySearch(lst,key):
    l = 0
    h = len(lst) - 1
    while l <= h:
        mid = (l + h ) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            l = mid + 1
        else:
            h = mid - 1
    return -1




ele = 6
res = binarySearch([1,2,3,4,5,6,7,8,9,10],ele)
if res == -1:
    print(f"{ele} is not found")
else:
    print(f"{ele} found at :{res}")
