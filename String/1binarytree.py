

class Node:
    def __init__(self ,val): 
        self.val =val 
        self.left =None 
        self.right = None
n0 = Node(100) 
n1 = Node(50) 
n2 = Node(50)  
n3 = Node(5) 
n4 = Node(10)  
n6 = Node(5) 
n7 = Node(10)  

n0.left = n1 
n0.right = n2 
n1.left = n3 
n1.right= n4 
n2.right = n6 
n2.left = n7 

print(n0.val) 
print(n0.left.val)
print(n1.val)