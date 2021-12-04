def LDS(l):
    n = len(l)
    ldscount = [1] * n
    prev = [None] * n
    for i in range(n):
        premax = l[0]
        for j in range(i):
            if l[j] > l[i] and ldscount[j] > premax:
                premax,prev[i] = ldscount[j],j
        ldscount[i] = 1 + premax
    mx = max(ldscount)
    mxi = ldscount.index(mx)
    seq = []
    while mxi != None:
        seq.append(l[mxi])
        mxi = prev[mxi]
    return seq[::-1]