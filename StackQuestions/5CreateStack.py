class Stack :
    def __init__(self ):
        self.items = [] 

    def is_empty(self) :
        return len(self.items) ==0 
    
    def push(self, item) :
        self.items.append(item)  
    
    def pop(self) :
        if len(self.items ) ==0:
            return "Cannot pop stack is empty" 

        d =self.items.pop() 
        return d 
    
    def top(self):
        if len(self.items) ==0:
            return "stack is empty" 
        return self.items[-1] 
    
    def size(self):
        return len(self.items) 
    
    
    def __str__(self):
        return f"Stack: {self.items}"

s = Stack() 
print(s.is_empty()) 
s.push(4)
print(s)
print(s.pop())