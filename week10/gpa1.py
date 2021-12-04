def findContinuosRepetitions(t,p):
    last = {}
    m = len(p)
    for i in range(m):
        last[p[i]] = i
    poslist,i,count,maxr = [],0,0,0
    while i <= (len(t) - m):
        matched,j = True,len(p) - 1
        poslist.append(i)
        while j > 0 and matched:
            if t[i+j] != p[j]:
                matched = False
                count = 0
            j = j - 1
        if matched:
            count += 1
            if (count > maxr):maxr = count
            i = i + m
        else:
            j = j + 1
            if t[i+j] in last.keys():
                 i = i + max(j-last[t[i+j]],1)
            else:
                i = i + j + 1
    return maxr

t = input()
p = input()
print(findContinuousRepetitions(t, p))