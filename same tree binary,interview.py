class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree( p, q) :
        
    if p == None and q == None:
            return True
    elif p == None or q == None:
        return False
    elif p.val == q.val:
        return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))
    else:
        return False



root1 = TreeNode(1) 
root2 = TreeNode(9) 
root1.left = TreeNode(2) 
root1.right = TreeNode(3) 
root1.left.left = TreeNode(4) 
root1.left.right = TreeNode(5) 
  
root2.left = TreeNode(2) 
root2.right = TreeNode(3) 
root2.left.left = TreeNode(4) 
root2.left.right = TreeNode(5) 

print(isSameTree(root1, root2))