# count=0
# curr = head

# while curr:
#     count+=1
#     curr=curr.next

# #case-1
# if count==1:
#     head = None
#     return head

# #case-2
# if count <=n:
#     head=head.next
#     return head

# l = count - n
# b = head

# for i in range(0,l-1):
#     b = b.next
    
# b.next = b.next.next

# return head

class Node:
    def __init__(self,val):
        self.val1=val
        self.next=None
        
def removeNthFromEnd(head, n):
    curr = head

    while curr:
        count+=1
        curr=curr.next

    #case-1
    if count==1:
        head = None
        return head

    #case-2
    if count <=n:
        head=head.next
        return head

    l = count - n
    b = head

    for i in range(0,l-1):
        b = b.next
        
    b.next = b.next.next

    return head
        

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)

print(removeNthFromEnd(head,2))