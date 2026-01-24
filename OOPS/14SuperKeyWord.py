class Phone:
    def __init__(self, price, brand,camera):  
        print("Inside Phone")
        self.price = price 
        self.brand = brand 
        self.camera = camera 
    
    def buy(self) :
        print("buying a phone")
        
class SmartPhone(Phone): 
    def __init__(self,name,price,brand,camera) : 
        super().__init__(price,brand,camera) 
        print("Inside child ")
        self.name = name
       
      
    def buy(self) :
        print("buying a SmartPhonephone")
        super().buy()
        
s = SmartPhone('oppo',123,'MI','50 MP') 
print(s.brand ,s.price ,s.camera)  
s1= SmartPhone("MI",123,'MI','50 MP') 
print(s1.name)
s1.buy()