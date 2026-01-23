class Person:
    def __init__(self):
        self.__name = "" 
        self.__age = "" 

    def get_age(self): 
        return self.__age 
    
    def set_age(self,new_val) :
        try:
            if type(new_val) != int :
                raise TypeError("Value should be valid integer") 
            if new_val<0 : 
                raise ValueError("Value Should greater than 0 ") 
            
            self.__age = new_val 
            print("Value set successfully")
        except Exception as e : 
            print("Error ",e)
     
p1 = Person() 
print(p1.get_age()) 
p1.set_age(11) 
print(p1.get_age())
 
                 

