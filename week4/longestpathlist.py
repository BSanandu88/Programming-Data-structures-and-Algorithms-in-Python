# Longest path using adjaceny list

def longestpathlist(AList):
    (indegree,lpath) = ({},{})
    for u in AList.keys():
        (indegree[u],lpath[u]) = (0,0)
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    
    zerodegreeq = Queue() // queue
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)
    
    while (not zerodegreeq.isempty()):
        j = zerodegreeq.delq()
        indegree[j] = indegree[j] - 1
        for k in AList[j]:
            indegree[k] = indegree[k] - 1
            lpath[k] = max(lpath[k],lpath[j] + 1)
            if indegree[k] == 0:
                zerodegreeq.addq(k)
    return(lpath)