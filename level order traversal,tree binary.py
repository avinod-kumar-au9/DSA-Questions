class Node:
    def __init__(self, val): 
        self.val = val  
        self.left = None  
        self.right = None

def height(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return 1
    else:
        return 1+max(height(root.left),height(root.right))

def levelOrder(root):
    h=height(root)
    for i in range(1,h+1):
        printlevel(i,root)

def printlevel(leve,root):
    if root==None:
        return
    if leve==1:
        print(root.val,end=" ")
    elif leve>1:
        printlevel(leve-1,root.left)
        printlevel(leve-1,root.right)

root= Node(1)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)

height(root)

levelOrder(root)
