class Node:
    def __init__(self ,val): 
        self.val = val 
        self.next = None 


class SLL:
    def __init__(self):
        self.head = None 

    def append(self,val) :
        new_node = Node(val) 
        if self.head ==None :  
            self.head = new_node 
        else : 
            curr = self.head 
            while(curr.next is not None):
                curr = curr.next
            curr.next= new_node 
    
    def traversal(self) : 
        if self.head is None:
            print("SLL is Empty") 
        else: 
            curr = self.head
            while(curr is not None) :
                print(curr.val ,end = " ") 
                curr =curr.next 

    def insert(self,index,val):
        new_node=Node(val) 
        if index ==0:
            new_node.next = self.head
            self.head = new_node 
        else:
            prev = None
            curr = self.head 
            count = 0 
            while(curr is not None and count<index):
                prev = curr 
                curr = curr.next 
                count=count +1 
            prev.next = new_node 
            new_node.next = curr


    def deletion(self,val):  
        curr = self.head  
        if self.head is None:
            print("SLL is empty")
            return

        # if head needs to be deleted
        if self.head.val == val:
            temp = self.head
            self.head = self.head.next
            del temp
            return
        if self.head is None : 
            self.head = curr.next  
            del curr 
            return 
        else:
            found = False 
            prev = None 
            while (curr is not None) :
                if curr.val == val:
                    found = True 
                    break 
                prev = curr 
                curr = curr.next 
            if found :
                prev.next = curr.next 
                del curr 
                return 
            else:
                print("Node not Found") 
    def middle_find (self) :
        curr = self.head 
        if self.head == None:
            print("Linklist is empty") 
            return 
        else: 
            n= 0  
            while(curr is not None) :  
                n= n+1 
                curr = curr.next  
            
            middle = n//2  
            for i in range(0, middle ) : 
                curr = curr.next  
            return curr
             
    def middle_find_opti(self) : 
        curr = self.head 
        fast = self.head 
        if self.head == None :
            print("SLL is empty") 
            return
         
        else:  
            while(fast is not None and fast.next is not None) :
                curr = curr.next 
                fast = fast.next.next  
            return curr
            
            


     


n1 = Node(2)
n2 = Node(3) 
n3 = Node(4)
n1.next = n2 
n2.next = n3 
print(n1.val) 
print(n2.val) 
print(n1.next) 
print(n1.next.val) 
print(n2) 
print(n1.next.next.val) 

s = SLL()  
s.append(2)
s.append(12)
s.append(32)
s.append(12)
s.append(24)
s.middle_find()






 


