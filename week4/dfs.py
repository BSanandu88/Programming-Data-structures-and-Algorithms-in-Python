# DEPTH FIRST SEARCH

from typing import ValuesView


def DFSinit(Amat):
    # Initialisation
    (rows,cols) = Amat.shape
    (visited,parent) = ({},{})
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return(visited,parent)

def DFS(Amat,visited,parent,v):
    visited[v] = True
    for k in neighbours(Amat,v):
        if(not visited[k]):
            parent[k] = v
            (visited,parent) = DFS(Amat,visited,parent,k)
    return (visited,parent)


# Global method

(visited,parent) = ({},{})

def DFSInitGlobal(AMat):
    # Initialization
    (rows,cols) = AMat.shape
    for i in range(rows):
        visited[i] = False
        parent[i] = -1 
    return 

def DFSGlobal(AMat,v):
    visited[v] = True
    for k in neighbours(AMat,v):
        if(not visited[k]):
            parent[k] = v
            DFSGlobal(AMat,k)
    return

# Adjacency list

def DFSInitList(AList):
    (visited,parent) = ({},{})
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return(visited,parent)

def DFSList(AList,visited,parent,v):
    visited[v] = True
    for k in AList[v]:
        if(not visited[k]):
            parent[k] = v
            (visited,parent) = DFSList(AList,visited,parent,k)
    return (visited,parent)

# Global using adjacency list
(visited,parent) = ({},{})

def DFSInitListGlobal(AList):
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return

def DFSListGlobal(AList,v):
    visited[v] = True
    for k in AList[v]:
        if(not visited[k]):
            parent[k] = v
            DFSListGlobal(AList,k)
    return 