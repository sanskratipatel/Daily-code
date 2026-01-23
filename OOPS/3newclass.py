class GreetIndia:
    def __init__(self , name ,place): 
        self.name = name
        self.place = place 
    
    def greet(self) :
        print(f"My name is {self.name} and i am from {self.place}") 

c = GreetIndia('Abhi' , 'India')  
c.greet()
c.gender = 'female' 
print(c.gender) 