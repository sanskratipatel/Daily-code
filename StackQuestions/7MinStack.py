class MinStack : 
    def __init__(self) :
        self.items = []  
        

    def pop(self) :
        if len(self.items) ==0 :
            print("Cannot Pop stack is empty") 
        return self.items.pop() 
    
    def push(self,item):
        if len(self.items) ==0 :
            self.items.append([item , item]) 
        else:
            self.mini = min(self.items[-1][1] ,item ) 
            self.items.append([item, self.mini]) 

    def get_min(self) :
        if len(self.items) == 0: 
            return 0 
        return self.items[-1][1] 
    
    def top(self) : 
        if len(self.items) == 0: 
            return 0 
        return self.items[-1][0] 
    def __str__(self): 
        return self.items
        
s1 = MinStack() 
s1.push(2) 
s1.push(4) 
s1.push(5) 
print(s1.get_min())

