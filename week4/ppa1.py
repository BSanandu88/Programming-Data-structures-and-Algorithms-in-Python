# Given an undirected graph G , write a Python function to compute the number of connected
# components. A set of nodes form a connected component in an undirected graph if there exists a
# path between every pair of nodes in this set.
# Write a Python function findComponents_undirectedGraph(vertices, edges) , that accepts a
# list of vertices and a list of tuples that represent edges, and returns the number of connected
# components in the graph formed by vertices and edges . Each tuple (i,j) in edges
# represents an edge between vertices i and j

from collections import deque

class myQueue:
    def __init__(self):
        self.Q = deque()
    def deQueue(self):
        return self.Q.popleft()
    def enQueue(self,x):
        return self.Q.append(x)
    def isEmpty(self):
        return False if self.Q else True

def findcomponenets_undirectedgraph(vertices,edges):
    GList = {}   # adjacency list for graph
    for i in vertices:
        GList[i] = []
    for (i,j) in edges:
        GList[i].append(j)
        GList[j].append(i)
    # mark every vertex not visited
    visited = {v:False for v in vertices}
    q = myQueue()
    componentscount = 0
 # 1. Select some vertex v
# 2. Start traversing the graph from v, till all vertices are visited in
# this component. Increment component count.
# 3. Search for any unvisited vertex v, go to step 2
    for v in vertices:
        if not visited[v]:
            q.enQueue(v)
        while not q.isEmpty():
            v = q.deQueue()
            if not visited[v]:
                for i in GList[v]:
                    if(not visited[i]):
                        q.enQueue(i)
                visited[v] = True
        componentscount += 1
    return componentscount


v = [item for item in input().split(" ")]
numberofEdges = int(input())
e = []
for i in range(numberofEdges):
    s = input().split(" ")
    e.append((s[0],s[1]))
print(findcomponenets_undirectedgraph(v,e))
