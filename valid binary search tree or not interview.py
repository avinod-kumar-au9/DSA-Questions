class Node: 
  
    
    def __init__(self,val): 
        self.val = val 
        self.left = None
        self.right = None

def isValidBST(root):
    lisa=[]
    solve(root,lisa)
    for i in range(len(lisa)-1):
        if lisa[i] >= lisa[i+1]: 
            return False
    return True


def solve(root,lisa):
    
    if root is None:
        return
    
    solve(root.left,lisa)
    lisa.append(root.val)
    solve(root.right,lisa)
        

root = Node(2) 
root.left = Node(5) 
root.right = Node(3) 
# root.left.left = Node(1) 
# root.left.right = Node(3)


print(isValidBST(root))



