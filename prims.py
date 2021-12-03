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

# improved version
def primlist2(Wlist):
    infinity = 1 + max([d for u in Wlist.keys() for (v,d) in Wlist[u]])
    (visited,distance,nbr) = ({},{},{})
    for v in Wlist.keys():
        (visited[v],distance[v],nbr[v]) = (False,infinity,-1)
    visited[0] = True
    for (v,d) in Wlist[0]:
        (distance[v],nbr[v]) = (d,0)
    for i in range(1,len(Wlist.keys())):
        nextd = min([distance[v] for v in Wlist.keys() if not visited[v]])
        nextvlist = [v for v in Wlist.keys() if (not visited[v]) and distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        for (v,d) in Wlist[nextv]:
            if not visited[v]:
                (distance[v],nbr[v]) = (min(distance[v],d),nextv)
    return(nbr)
