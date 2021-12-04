def BFSlistPath(Alist,v,preventionList = []):
    visited,parent = {},{}
    for i in Alist.keys():
        visited[i] = False
        parent[i] = -1
    q = []
    visited[v] = True
    q.append(v)
    while len(q) > 0:
        j = q.pop(0)
        for k in Alist[j]:
            if not visited[k] and not k in preventionList:
                visited[k] = True
                parent[k] = j
                q.append(k)
    return visited,parent

def findpath(parent,start,end):
    l = []
    curr = parent[end]
    while curr != start:
        l.append(curr)
        curr = parent[curr]
    return l

def backandforth(Alist,start,end):
    preventionList = []
    visited,parent = BFSlistPath(Alist,start,preventionList)
    c = 0
    while visited[end]:
        c += 1
        path = findpath(parent,start,end)
        preventionList.extend(path)
        visited,parent = BFSlistPath(Alist,start,preventionList)
    return c

start = int(input())
end = int(input())
AList = {}
while True:
    line = input()
    if line.strip() == '':
        break
    u, vs = line.strip().split(':')
    u = int(u)
    AList[u] = []
    for v in vs.strip().split():
        v = int(v)
        if v not in AList:
            AList[v] = []
        AList[u].append(v)
print(backandforth(AList, start, end))