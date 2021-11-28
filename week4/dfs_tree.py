(visited,pre,post) = ({},{},{})

def DFSInitPrePost(AList):
    for i in AList.keys():
        visited[i] = False
        (pre[i],post[i]) = (-1,-1)
    return

def DFSPrePost(AList,v,count):
    visited[v] = True
    pre[v] = count
    count = count + 1
    for k in AList[v]:
        if(not visited[k]):
            count = DFSPrePost(AList,k,count)
    post[v] = count
    count = count + 1

    return count