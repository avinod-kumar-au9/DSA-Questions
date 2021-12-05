class Node:
    def __init__(self,val):
        self.val1=val
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def printLL(self):
        if self.head is None:
            print("list has no element")
            return
        else:
            cur = self.head
            while cur != None:
                print(cur.val1, " ")
                cur = cur.next

    def addelements_to_end_ll(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        cur= self.head
        while cur.next != None:
            cur=cur.next
        cur.next = new_node

    # def taking_user_input_forvalues_tocreate_ll(self):
    #     nums = int(input("How many nodes do you want to create: "))
    #     if nums == 0:
    #         return
    #     for i in range(nums):
    #         value = int(input("Enter the value for the node:"))
    #         self.addelements_to_end_ll(value)

    def addelements_to_start_ll(self,val):
        new_node= Node(val)
        new_node.next = self.head
        self.head = new_node

    def addelement_after_specific_element(self,x, val):
        cur = self.head
        # print(cur.next)
        while cur != None:
            if cur.val1 == x:
                break
            cur= cur.next
        if cur is None:
            print("item not in list")
        else:
            new_node = Node(val)
            new_node.next= cur.next
            cur.next = new_node

    def addelement_before_specific_element(self,x, val):
        if self.head is None:
            print("list has no element")
            return
        
        # if self.head.next == x:
        #     new_node= Node(val)
        #     new_node.next = self.head
        #     self.head= new_node
        #     return

        cur= self.head
        print(cur.next)
        while cur.next != None:
            if cur.next.val1==x:
                break
            cur= cur.next
        if cur.next is None:
            print("item not in list")
        else:
            new_node = Node(val)
            new_node.next= cur.next
            cur.next = new_node

    def addelement_at_specific_index(self,index,val):
        
        i = 1
        cur = self.head
        while i < index-1 and cur is not None:
            cur = cur.next
            i = i+1
        if cur is None:
            print("Index out of bound")
        elif index == 1:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else: 
            new_node = Node(val)
            new_node.next = cur.next
            cur.next = new_node

    def delete_element_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return 
        self.head = self.head.next

    def delete_element_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return

        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None

    def delete_element_by_value(self, x):
        if self.head is None:
            print("The list has no element to delete")
            return

        # Deleting first node 
        if self.head.val1 == x:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next is not None:
            if cur.next.val1 == x:
                break
            cur = cur.next

        if cur.next is None:
            print("item not found in the list")
        else:
            cur.next = cur.next.next

    def reverse_linkedlist(self):
        prev = None
        cur = self.head
        while cur is not None:
            nextval = cur.next
            cur.next = prev
            prev = cur
            cur = nextval
        self.head = prev

    def finding_middle_element(self):
        bow = self.head
        cur= self.head
        while bow != None and cur != None and cur.next != None:
            bow= bow.next
            cur=cur.next.next
        print("middle value",bow.val1)

    def finding_n_node_fromthe_end(self,n):
        cur=self.head
        cnt=0
        while cur != None:
            cnt+=1
            cur=cur.next
        
        if n > cnt:
            print("-1")
        else:
            cur=self.head
            for i in range(0,cnt-n):
                cur=cur.next
            print("nth Node",cur.val1)
    

if __name__ == "__main__":
    new_linked_list= Linkedlist()

    # new_linked_list.taking_user_input_forvalues_tocreate_ll()

    new_linked_list.addelements_to_end_ll(5)
    new_linked_list.addelements_to_end_ll(10)
    new_linked_list.addelements_to_end_ll(15)

    # new_linked_list.addelements_to_start_ll(2)

    # new_linked_list.addelement_after_specific_element(10, 25)

    # new_linked_list.addelement_before_specific_element(10,32)

    new_linked_list.addelement_at_specific_index(2, 50)

    # new_linked_list.delete_element_at_start()

    # new_linked_list.delete_element_at_end()

    # new_linked_list.delete_element_by_value(5)
    # new_linked_list.printLL()

    # new_linked_list.reverse_linkedlist()

    # new_linked_list.finding_middle_element()

    # new_linked_list.finding_n_node_fromthe_end(3)

    new_linked_list.printLL()
    