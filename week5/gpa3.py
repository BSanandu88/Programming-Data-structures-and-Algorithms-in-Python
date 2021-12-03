''' Negative edge weight problems'''

def IsNegativeWeightCyclePresent(WList):
    s = 0
    infinity = 1 + len(WList.keys()) * max([d for u in WList.keys() for (v,d) in WList[u]])
    distance = {}
    for v in WList.keys():
        distance[v] = infinity
    distance[s] = 0
    for i in WList.keys():
        for u in WList.keys():
            for (v,d) in WList[u]:
                distance[v] = min(distance[v],distance[u] + d)
    
    for u in WList.keys():
        for (v,d) in WList[u]:
            if (distance[u] + d < distance[v]):
                return True
    return False

size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
print(WL)
print(IsNegativeWeightCyclePresent(WL))
'''5
[(0,1,10),(0,2,-5),(0,3,2),(3,2,-5),(2,1,-20),(1,3,10)]
{0: [(1, 10), (2, -5), (3, 2)], 1: [(3, 10)], 2: [(1, -20)], 3: [(2, -5)], 4: []}
True'''