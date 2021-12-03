def primlist(Wlist):
    infinity = 1 + max([d for u in Wlist.keys() for (v,d) in Wlist[u]])
    (visited,distance,treeEdges) = ({},{},{})
    for v in Wlist.keys():
        (visited[v],distance[v]) = (False,infinity)
    visited[0] = True
    for (v,d) in Wlist[0]:
        distance[v] = d
    for i in Wlist.keys():
        (mindlist,nextv) = (infinity,None)
        for u in Wlist.keys():
            for (v,d) in Wlist[u]:
                if visited[u] and (not visited[v]) and d < mindlist:
                    (mindlist,nextv,nexte) = (d,v,(u,v))
        if nextv is None:
            break
        visited[nextv] = True
        treeEdges.append(nexte)
        for (v,d) in Wlist[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v],d)
    return(treeEdges)
