''' merge k list into single list'''
from _typeshed import ReadOnlyBuffer
from typing import Sized


class min_heap:
    def __init__(self) -> None:
        self.size = 0
        self.arr = []
    def isempty(self):
        return True if (self.size == 0) else False
    # heapify
    def heapify_down(self,i):
        n = self.size
        a = self.arr
        while(i < n):
            ss = l = 2 * i + 1
            r = 2 * i + 2
            if (l < n and r < n and a[l][0] > a[r][0]):
                ss = r
            if (ss < n and a[ss][0] < a[i][0]):
                a[i],a[ss] = a[ss],a[i]
                i = ss
            else:
                break
    
    def delete_min(self):
        min = self.arr[0]
        last = self.arr.pop()
        self.size -= 1
        if (self.size > 0):
            self.arr[0] = last
            self.heapify_down(0)
        return min
    
    def heapify_up(self):
        i = self.size() - 1
        while(i > 0):
            parent = (i-1)/2
            if (self.arr[i][0] < self.arr[parent][0]):
                self.arr[i],self.arr[parent] = self.arr[parent],self.arr[i]
                i = parent
            else:
                break
    def insert_min_heap(self,x):
        self.arr.append(x)
        self.size += 1
        self.heapify_up
    
def mergeKLists(L):
    K = len(L)
    h = min_heap()
    finalList = []
    for i in range(k):
        tup = (L[i][0],i)
        h.insert_min_heap(tup)
    kp = [l for i in range(k)]
    while (not h.isempty()):
        tup = h.delete_min()
        finalList.append(tup[0])
        listn = tup[1]
        if (kp[listn] < len(L[listn])):
            tup = (L[listn][kp[listn]],listn)
            h.insert_min_heap(tup)
            kp[listn] += 1
    return finalList


# EASIER METHOD

def partition(array,low,high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= pivot:
            i = i+1
            (array[i],array[j]) = (array[j],array[i])
    (array[i+1],array[high]) = (array[high],array[i+1])
    return i+1


def quickSort(array,low,high):
    if low < high:
        p = partition(array,low,high)
        quickSort(array,low,p-1)
        quickSort(array,p+1,high)


def mergeKlist(l):
    sl = list()
    for i in l:
        sl.extend(i)
    quickSort(sl,0,len(sl) - 1)
    return sl


k = int(input())
ll = []
for i in range(k):
    subl = [int(item) for item in input().split(" ")]
    ll.append(subl)
print(*mergeKLists(ll))