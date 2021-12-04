# 1st solution

def no_overlap(l):
    l.sort(key = lambda x : x[2])
    result = []
    result.append(l[0][0])
    start = 0
    finish = 1
    while((start != len(l)) and (finish != len(l))):
        if (l[start][2] < l[finish][1]):
            result.append(l[finish][0])
            start = finish
            finish = finish - 1
        else:
            finish = finish + 1
    return result

# 2nd approach

def tuplesort(L, index):
    L_ = []
    for t in L:
        L_.append(t[index:index+1] + t[:index] + t[index+1:])
    L_.sort()

    L__ = []
    for t in L_:
        L__.append(t[1:index+1] + t[0:1] + t[index+1:])
    return L__


def no_overlap2(l):
    sorted_l = tuplesort(l,2)
    accepted = [sorted_l[0][0]]
    for i,s,f in sorted_l[1:]:
        if s > l[accepted][-1][2]:
            accepted.append(i)
    return accepted