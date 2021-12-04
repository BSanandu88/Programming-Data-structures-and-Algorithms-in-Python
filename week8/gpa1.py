# 1 method

def first(arr,x,n):
    low = 0
    high = n - 1
    res = None
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid - 1
        else:
            res = mid
            high = mid - 1
    return res

def last(arr,x,n):
    low = 0
    high = n - 1
    res = None
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res

def findOccOf(l,x):
    return (first(l,x,len(l)),last(l,x,len(l)))

A = [int(item) for item in input().split(" ")]
x = int(input())
print(findOccOf(A,x))

