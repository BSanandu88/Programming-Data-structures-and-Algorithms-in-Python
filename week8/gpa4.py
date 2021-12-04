

def partitionpos(arr,pivot):
    arr[pivot],arr[0] = arr[0],arr[pivot]
    l =  1
    r = len(arr) - 1
    while(l < r):
        while(arr[l] < arr[0]):
            l += 1
        while(arr[r] >= arr[0]):
            r -= 1
        arr[l],arr[r] = arr[r],arr[l]
    return l-1

def MoM7(arr):
    if len(arr) <= 7:
        arr.sort()
        return(arr[len(arr) // 2])
    m = []
    for i in range(0,len(arr),7):
        x = arr[i:i+7]
        x.sort()
        m.append(x[len(x)//2])
    return (MoM7(m))

def MoM7Pos(arr):
    mom = MoM7(arr)
    return partitionPos(arr,arr.index(mom))

arr = [int(item) for item in input().split(" ")]
print(MoM7Pos(arr))