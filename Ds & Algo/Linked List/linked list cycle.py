"""
Question : https://leetcode.com/problems/linked-list-cycle/
"""



class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
def cycle(root):
    slow = root
    fast = root
    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False
    
        
        
        
root=Node(1)
root.next=Node(2)
root.next.next=Node(5)

print(cycle(root))