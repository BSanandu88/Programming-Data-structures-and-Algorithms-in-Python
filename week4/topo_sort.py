# Topological Sorting

def toposort(AMat):
    (rows,cols) = AMat.shape
    indegree = {}
    toposortlist = []
    for c in range(cols):
        indegree[c] = 0
        for r in range(rows):
            if AMat[r,c] == 1:
                indegree[c] = indegree[c] + 1
    
    for i in range(rows):
        j = min([k for k in range(cols)
                 if indegree[k] == 0])
        toposortlist.append(j)
        indegree[j] = indegree[j] - 1
        for k in range(cols):
            if AMat[j,k] == 1:
                indegree[k] = indegree[k] - 1
    return (toposortlist)

# topo sort using adjacency list
import queue

def toposortlist(AList):
    (indegree,toposortlist) = ({},[])
    for u in AList.keys():
        indegree[u] = 0
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    
    zerodegreeq = queue()
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)
    
    while (not zerodegreeq.isempty()):
        j = zerodegreeq.delq()
        toposortlist.append(j)
        indegree[j] = indegree[j] - 1
        for k in AList[j]:
            indegree[k] = indegree[k] - 1
            if indegree[k] == 0:
                zerodegreeq.addq(k)
    return (toposortlist)