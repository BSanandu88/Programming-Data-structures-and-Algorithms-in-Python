# Long journey
# A tourist wants to travel around India from north to south. He has a policy that he never travels
# back towards the north. Write a Python function longJourney(AList) to find him a route with
# which he can visit the maximum number of cities according to his policy, where AList represents
# a graph of cities and routes between them. Every edge in adjacency list AList is a feasible route
# between one city to another from north to south. The function should return a list in the order
# the cities are to be visited to visit maximum cities.

# 1st method
class Queue:
    def __init__(self):
        self.queue = []
    def isempty(self):
        return self.queue == []
    def addq(self,v):
        self.queue.append(v)
    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v

def find_northmost_city(AList):
    destinations = []
    for dest_list in AList.values():
        dest_cities = [city for city in dest_list]
        destinations += dest_cities
    northmost_city = [city for city in AList.keys() if city not in destinations]
    return northmost_city[0]

def allPathsFound(paths,AList):
    for path in paths:
        if AList[path[-1]] != []:
            return False
    return True

def findAllPaths(AList):
    curr = find_northmost_city(AList)
    path = [curr]
    paths = [path]
    while not allPathsFound(paths,AList):
        paths2 = paths.copy()
        paths = []
        for path in paths2:
            curr = path[-1]
            if AList[curr] == []:
                paths.append(path)
                continue
            for node in AList[curr]:
                if node in path:
                    continue
                else:
                    path.append(path + [node])
    return paths

def longJourney(AList):
    paths = findAllPaths(AList)
    max_path_length = max([len(path) for path in paths])
    for path in paths:
        if(len(path) == max_path_length):
            return path


# 2nd method

class Queue:
    def __init__(self):
        self.queue = []
    def addq(self,v):
        self.queue.append(v)
    def delq(self):
        v = None
        if not in self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
            return v
    def isempty():
        return self.queue == []
    def __str__(self):
        return str(self.queue)

#Dictionary inversion
def dInv(d):
    d1= {}
    if not isinstance(list(d.values())[0],list):
        for k,v in d.items():
            if v not in d1:
                d1[v] = []
            d1[v].append(k)
        return d1
    
    if isinstance(list(d.values())[0],list):
        for k,v in d.items():
            for v1 in v:
                d1[v1] = []
            d1[v1].append(k)
        return d1

# Longest path function from the lecture
def longestpath(AList):
    indegree,lpath = {},{}
    for u in AList:
        indegree[u],lpath[u] = 0,0
    for u in AList:
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    zerodegreeq = Queue()
    for u in AList:
        if indegree[u] == 0:
            zerodegreeq.addq(u)
    while not zerodegreeq.isempty():
        j = zerodegreeq.delq()
        indegree[j] = indegree[j] - 1
        for k in AList[j]:
            indegree[k] = indegree[k] - 1
            lpath[k] = max(lpath[k],lpath[j] + 1)
            if indegree[k] == 0:
                zerodegreeq.addq(k)
    return lpath

def longjourney(AList):
    lpath = longestpath(AList)
    IAList = dInv(AList)
    Llj = dInv(lpath)
    maxVal = max(lpath.values())
    prev = Llj[maxVal][0]
    path = [prev]
    for i in range(maxVal,-1,-1):
        for p in Llj[i]:
            if p in IAList[prev]:
                path.append(p)
                prev = p
    return path[::-1]


