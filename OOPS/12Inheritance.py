class Phone:
    def __init__(self, price, brand,camera):  
        print("Inside Phone")
        self.price = price 
        self.brand = brand 
        self.camera = camera 
    
    def buy(self) :
        print("buying a phone")
        
class SmartPhone(Phone): 
    def __init__(self,name) : 
        self.name = name
        

# s = SmartPhone(123,'MI','50 MP') 
# print(s.brand ,s.price ,s.camera)  
s1= SmartPhone("MI") 
print(s1.name)
s1.buy()