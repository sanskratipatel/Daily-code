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

    def reverse_ll(self) : 
        if self.head is None:
            print("LL is empty") 
            return 
        temp = self.head 
        prev = None 
       
        while(temp is not None): 
            front = temp.next
            temp.next =prev  
            prev = temp 
            temp = front 
       

 

    


        


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