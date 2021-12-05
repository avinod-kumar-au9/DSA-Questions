class Node: 
    def __init__(self , key): 
        self.key = key 
        self.left = None
        self.right = None
  
def isFullTree(root): 
    if root is None:     
        return True
      
    if root.left is None and root.right is None: 
        return True

    if root.left is not None and root.right is not None: 
        return (isFullTree(root.left) and isFullTree(root.right)) 
      
    return False
  

root = Node(10); 
root.left = Node(20); 
root.right = Node(30); 
  
root.left.right = Node(40); 
root.left.left = Node(50); 
# root.right.left = Node(60); 
# root.right.right = Node(70); 
  

  
if isFullTree(root): 
    print ("The Binary tree is full")
else: 
    print ("Binary tree is not full")

print(isFullTree(root))