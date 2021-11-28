# Identifying connected components


def BFSList(AList,v):   # Adjacency list 
    visited = {}
    for i in AList.keys():
        visited[i] = False
    q = Queue()
    visited[v] = True
    q.addq(v)
    while(not q.isempty()):
        j = q.delq()
        for k in AList[j]:
            if(not visited[k]):
                visited[k] = True
                q.addq(k)

    return(visited)

def Components(AList):
    component = {}
    for i in AList.keys():
        component[i] = -1

    (compid,seen) = (0,0)
    while seen <= max(AList.keys()):
        startv = min([i for i in AList.keys()
                     if component[i] == -1 ])
        visited = BFSList(AList,startv)

        for i in visited.keys():
            if visited[i]:
                seen = seen + 1
                component[i] = compid
        compid = compid + 1
    return(component)
