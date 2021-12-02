
# 1 METHOD
from typing import TYPE_CHECKING


def FiberLink(WL):
    infinity = 1 + max([d for u in WL.keys() for (v,d) in WL[u]])
    (visited,distance,treeEdges) = ({},{},{})
    totalDist = 0
    for v in WL.keys():
        (visited[v],distance[v]) = (False,infinity)
    
    visited[0] = True
    for (v,d) in WL[0]:
        distance[v] = d
    for i in WL.keys():
        (mindist,nextv) = (infinity,None)
        for u in WL.keys():
            for (v,d) in WL[u]:
                if visited[u] and (not visited[v]) and d < mindist:
                    (mindist,nextv,nexte) = (d,v,(u,v))
        
        if nextv is None:
            break
        totalDist += mindist
        visited[nextv] = True
        treeEdges.append(nexte)

        for (v,d) in WL[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v],d)
    return totalDist

size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = {}
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))

