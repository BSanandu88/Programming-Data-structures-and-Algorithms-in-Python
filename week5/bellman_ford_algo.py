
import numpy as np

def bellmanford(WMat,s):
    (rows,cols,x) = WMat.shape
    infinity = np.max(WMat) * rows + 1
    distance = {}
    for v in range(rows):
        distance[v] = infinity
    distance[s] = 0

    for i in range(rows):
        for u in range(rows):
            for v in range(cols):
                if WMat[u,v,0] == 1:
                    distance[v] = min(distance[v],distance[u] + WMat[u,v,1] )
    return(distance)
