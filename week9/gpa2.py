# matrix 

def maxcoinpath(m,x1,y1,x2,y2):
    mcp = []
    for i in range(len(m)):
        l = []
        for j in range(m[0]):
            l.append(0)
        mcp.append(l)
    mcp[x1][y1] = m[x1][y1]
    for i in range(y1+1,len(m[0])):
        mcp[x1][i] = mcp[x1][i-1] + m[x1][i]
    for i in range(x1+1,len(m[0])):
        mcp[i][y1] = mcp[i-1][y1] + m[i][y1]
    for i in range(x1+1,len(m)):
        for j in range(y1+1,len(m[0])):
            mcp[i][j] = max(mcp[i-1][j],mcp[i][j-1]) + m[i][j]
    return mcp[x2][y2]


m = eval(input())
(x1,y1) = eval(input())
(x2,y2) = eval(input())
print(maxcoinpath(m,x1,y1,x2,y2))