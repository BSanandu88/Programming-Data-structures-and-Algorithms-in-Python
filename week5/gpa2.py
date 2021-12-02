''' GPA 2
    DIJKSTRA ALGORITHM '''

from _typeshed import ReadOnlyBuffer
from week5.gpa1 import WL


def dijkstra(Wlist,s):
    infinity = 1 + len(Wlist.keys()) * max([d for u in Wlist.keys() for (v,d) in Wlist[u]])
    (visited,distance,prev) = ({},{},{})
    for v in Wlist.keys():
        (visited[v],distance[v],prev[v]) = (False,infinity,None)
    distance[s] = 0
    for u in Wlist.keys():
        nextd = min([distance[v] for v in Wlist.keys() if not visited[v]])
        nextvlist = [v for v in Wlist.keys() if (not visited[v]) and distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        for (v,d) in Wlist[nextv]:
            if not visited[v]:
                if distance[v] > distance[nextv] + d:
                    distance[v] = distance[nextv] + d
                    prev[v] = nextv
    return(distance,prev)

def min_cost_walk(WList,S,D,V):
    distance1,path1 = dijkstra(WList,S)
    distance2,path2 = dijkstra(WList,V)
    total_dist = distance1[V] + distance2[D]
    route_sv = []
    route_vd = []
    if distance1[V] != 0:
        dest = V
        while dest != S:
            route_sv = [dest] + route_sv
            for i,j in path1.items():
                if dest == i:
                    dest = j
                    break
        route_sv = [dest] + route_sv
    if distance2[D] != 0:
        dest = D
        while dest != V:
            route_vd = [dest] + route_vd
            for i,j in path2.items():
                if dest == i:
                    dest = j
                    break
        route_vd = [dest] + route_vd
    route_sv = route_sv[:-1] + route_vd
    return (total_dist,route_sv)

size = int(input())
edges = eval(input())
S= int(input())
D=int(input())
V=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(min_cost_walk(WL,S, D, V))
