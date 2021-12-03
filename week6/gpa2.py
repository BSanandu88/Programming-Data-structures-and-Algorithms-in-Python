# bst

class Tree:
    #constructor
    def __init__(self,initval = None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = self.right = None
        return
    
    # only empty node has value none
    def isempty(self):
        return(self.value == None)
    
    # leaf nodes have both children empty
    def isleaf(self):
        return(self.value != None and self.left.isempty() and self.right.isempty())
    
# insert into bst
def insertToBST(root,x):
    temp = root
    while(not temp.isempty()):
        if (x < temp.value):
            temp = temp.left
        else:
            temp = temp.right
    temp.value = x
    temp.left = Tree()
    temp.right = Tree()

def maxLessThan(root,k):
    if root.value == k:
        return root.value
    if root.isleaf():
        if root.value < k:
            return root.value
        else:
            return None
    if root.value > k:
        if root.left.isempty():
            return None
        else:
            return maxLessThan(root.left,k)
    else:
        temp = maxLessThan(root.right,k)
        if temp == None:
            return root.value
        else:
            return temp


l = [int(item) for item in input().split(" ")]
x = int(input())
root = Tree(l[0])
for item in l[1:]:
    insertToBST(root,item)
print(maxLessThan(root,x))