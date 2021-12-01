
import numpy as np

def bellmanford(WMat,s):
    (rows,cols,x) = WMat.shape
    infinity = np.max(WMat) * rows + 1
    distance = {}
    for v in range(rows):
        distance[v] = infinity
    distance[s] = 0

    for i in range(rows):
        for u in range(rows):
            for v in range(cols):
                if WMat[u,v,0] == 1:
                    distance[v] = min(distance[v],distance[u] + WMat[u,v,1] )
    return(distance)


# using adjaceny list

def bellmanfordlist(WList,s):
    infinity = 1 + len(WList.keys()) * max([d for u in WList.keys()
                                             for (v,d) in WList[u]])
    distance = {}
    for v in WList.keys():
        distance[v] = infinity
    distance[s] = 0
    for i in WList.keys():
        for u in WList.keys():
            for (v,d) in WList[u]:
                distance[v] = min(distance[v],distance[u] + d)
    return(distance)