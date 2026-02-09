from abc import ABC , abstractmethod
class Burger :
    @abstractmethod
    def prepare(self):
        pass

class BasicBurger(Burger) :
    def __init__(self):
        pass 
    
    def prepare(self):
        return "Preparing Basic Burger" 
    
class StandardBurger(Burger) :
    def __init__(self):
        pass 
    def prepare(self):
        return "Preparing Standard Burger" 

class PreminumBurger(Burger) :
    def __init__(self):
        pass 
    
    def prepare(self):
        return "Preparing Preminum Burger" 
    

class BurgerFactory:
    @staticmethod
    def create_burger( type_burger) : 
        type_burger = type_burger.lower()
        if type_burger == "basic": 
            return BasicBurger() 
        elif type_burger == "standard": 
            return StandardBurger() 
        elif type_burger == "preminum": 
            return PreminumBurger() 
        else:
            print("Invalid Burger Type") 
            return None 
        
c1 = BurgerFactory.create_burger("standarD")
print(c1.prepare())

    
    