
def binarySearch(lst,l,h,key):
 
    while l <= h:
        mid = (l + h ) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            return binarySearch(lst,mid+1 ,h,key)
        else:
            return binarySearch(lst,l,mid-1,key)
    return -1



ele = 6
res = binarySearch([1,2,3,4,5,6,7,8,9,10],0,7,ele)
if res == -1:
    print(f"{ele} is not found")
else:
    print(f"{ele} found at :{res}")
