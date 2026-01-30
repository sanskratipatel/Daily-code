class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 
    

class SLL :
    def __init__(self): 
        self.head = None 
    
    def append(self,item) :
        new_node = Node(item) 
        if self.head ==None:
            self.head = new_node 
        
        else:
            curr = self.head 
            while(curr.next is not None) :
                curr = curr.next 
            curr.next = new_node
        
    def traversal(self) :
        if self.head == None:
            print("LL IS Empty") 
        else:
            curr = self.head 
            count = 0
            while(curr is not None):
                print(curr.val , end = " ") 
                curr = curr.next 
    
    def insert(self,index,val) :
        new_node = Node(val) 
        if index ==0 :
            new_node.next = self.head 
            self.head = new_node 
        else:
            curr = self.head 
            prev = None 
            count = 0 
            while(curr is not None and count < index) : 
                prev = curr 
                curr = curr.next 
                count = count +1  
            prev.next = new_node 
            new_node.next = curr
    def deletions(self , val) :
        if self.head == None:
            print("LL IS EMPTY") 
            return 
        else:
            prev = None 
            curr = self.head 
            found = False 
            while(curr is not None) :
                if curr.val == val :
                    found = True 
                    break 
                prev = curr 
                curr = curr.next 
            if found == True :
                prev.next = curr.next 
                del curr  
            else :
                print("NOt found")
    def reverse (self) : 
        if self.head == None:
            print("Sll is Empty")
        curr = self.head 
        prev = None 
        while(curr is not None):
            front = curr.next 
            curr.next = prev 
            prev = curr 
            curr = front 
    def middle_find_opti(self) :
        if self.head == None:
            print("SLL is Empty") 
        else:
            curr = self.head
            fast = self.head 
            while(fast is not None and fast.next is not None) :  
                curr = curr.next 
                fast = fast.next.next
            return curr 
        
    def cycleLinkedList(self) : 
        if self.head ==None:
            print("SLL is Empty") 
        else:
            curr = self.head 
            fast = self.head  
            while(fast is not None and fast.next is not None):
                curr = curr.next 
                fast = fast.next.next 
                if curr == fast :
                    return True 
        return False

    # def start_point_cycle_brute(self) : 

