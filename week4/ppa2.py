# Complete the Python function findAllPaths to find all possible paths from the source vertex to
# destination vertex in a directed acyclic graph.
# Function findAllPaths(vertices, gList, source, destination) takes vertices as a list of vertices,
# gList a dictionary that is an adjacency List representation of graph edges, source vertex,
# destination vertex, and returns a list of all paths from source to destination . The return
# value will be a List of Lists, where every path is a sequence of vertices as a List. Return an empty
# list if no path exists from 'source' to 'destination'.

# Helper functions
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

# Function
def findAllPaths(vertices,glist,source,destination):
    allpaths = []
    path = []
    visited = {v:False for v in vertices}
    findAllPathsRecursive(vertices,glist,source,destination,visited,path,allpaths)
    return allpaths

def findAllPathsRecursive(vertices,glist,src,dest,visited,path,allpaths):
    visited[src] = True
    path.append(src)
    if(src == dest):
        allpaths.append(path.copy())
    for e in glist[src]:
        if not visited[e]:
            findAllPathsRecursive(vertices,glist,e,dest,visited,path,allpaths)
    path.pop()
    visited[src] = False

def ArrangeResult(result):
    res = []
    for item in result:
        s = ""
        for i in item:
            s += str(i)
        res.append(s)
    res.sort()
    return res

v = [item for item in input().split(" ")]
AList = {}
for i in v:
    AList[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()

print(ArrangeResult(findAllPaths(v,AList,source,dest)))