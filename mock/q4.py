def maxValueSelection(items,c):
    total_value = 0
    for i in sorted(items,key = lambda x : items[x][1]/items[x][0],reverse=True):
        if items[i][0] <= c:
            total_value += items[i][1]
            c -= items[i][0]
        else:
            total_value += items[i][1]/items[i][0] * c
            c = 0
    return total_value

# suffix
items = eval(input())
c = int(input())
print(int(maxValueSelection(items, c)))