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

