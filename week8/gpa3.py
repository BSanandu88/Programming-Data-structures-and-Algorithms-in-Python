import math

# Returns eucledian distance between points p and q
def distance(p, q):
  return math.sqrt(math.pow(p[0] - q[0],2) + math.pow(p[1] - q[1],2))

def minDistRec(px,py):
    s = len(px)
    if (s == 2):
        return distance(px[0],px[1])
    elif s == 3:
         return min(distance(px[0],px[1]), distance(px[1],px[2]), distance(px[2],px[0]))
    
    



def minDist(points):
    px = sorted(points)
    py = points
    py.sort(key = lambda x : x[-1])
    return round(minDistRec(px,py),2)


points = eval(input())
print(minDist(points))