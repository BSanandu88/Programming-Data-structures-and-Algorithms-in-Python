class Queue:
    def __init__(self):
        self.queue = []
    def addq(self,v):
        self.queue.append(v)
    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)
    def isempty(self):
        return(self.queue == [])
    def __str__(self):
        return (str(self.queue))

q = Queue()
for i in range(3):
    q.addq(i)
    print(q)
print(q.isempty())

for j in range(3):
    print(q.delq(),q)
print(q.isempty())

# BREADTH FIRST SEARCH


def BFS(Amat,v):
    (rows,cols) = Amat.shape
    visited = {}
    for i in range(rows):
        visited[i] = False
    q = Queue()
    visited[v] = True
    q.addq(v)

    while (not q.isempty()):
        j = q.delq()
        for k in neighbours(Amat,j):
            if (not visited[k]):
                visited[k] = True
                q.addq(k)
    return(visited)

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


# Path in bfs
def BFSListPath(AList,v):
    (visited,parents) = ({},{})
    for i in AList.keys():
        visited[i] = False
        parents[i] = -1
    q = Queue()
    visited[v] = True
    q.addq(v)
    while(not q.isempty()):
        j = q.delq()
        for k in AList[j]:
            if(not visited[k]):
                visited[k] = True
                parents[k] = j
                q.addq(k)
    return(visited,parents)


def BFSListPathLevel(Alist,v):
    (level,parent) = ({},{})
    for i in Alist.keys():
        level[i] = -1
        parent[i] = -1
    q = Queue()
    level[v] = 0
    q.addq(v)
    while(not q.isempty()):
        j = q.delq()
        for k in Alist[j]:
            if(level[k] == -1):
                level[k] = level[j] + 1
                parent[k] = j
                q.addq(k)
    return(level,parent)


