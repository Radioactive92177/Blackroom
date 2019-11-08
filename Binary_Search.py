#binary SEarch
def binarySearch(lst, l, r,x):
    while l <= r:
        mid = 1+(r-1)//2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            l = mid + 1
        else:
            r = mid -1
    return -1

a = []
b = int(input("Enter no of elements"))
for i in  range(b):
    c = int(input("Enter number one by one"))
    a.append(c)
x = int(input("enter element to be searched"))
result = binarySearch(a ,0 ,len(a)-1 , x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in list")