
''' GPA 2'''


def mergeAndCount(a,b):
    (m,n) = len(a),len(b)
    (c,i,j,k,count) = ([],0,0,0,0)
    while k < m+n:
        if i == m:
            c.append(b[j])
            (j,k) = (j+1,k+1)
        elif j == n:
            c.append(a[i])
            (i,k) = (i+1,k+1)
        elif a[i] < b[j]:
            c.append(a[i]) 
            (i,k) = (i+1, k+1)
        else:
            c.append(b[j])
            (j, k, count) = (j+1, k+1, count+(m-i))
  return (c,count)

def sortAndCount(A):
    n = len(A)
    if n <= 1:
        return(A,0)
    (l,countl) = sortAndCount(A[:n//2])
    (r,countr) = sortAndCount(A[n//2:])
    (b,countb) = mergeAndCount(l,r)
    return (b,countb + countl + countr)


def countIntersection(x1,x2):
    combined = [(x1[i],x2[i]) for i in range(0,len(x1))]
    combined.sort()
    x1,x2 = zip(*combined)
    return sortAndCount(X2)[1]

l1 = [int(i) for i in input().split(" ")]
l2 = [int(i) for i in input().split(" ")]
print(countIntersection(l1,l2))