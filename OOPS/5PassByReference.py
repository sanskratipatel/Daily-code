class PassByReference:
    def __init__(self , gender, name): 
        self.name = name 
        self.gender = gender 
    

def greet(PassByReference) :
    print(f"Hello {PassByReference.name} and my gender is {PassByReference.gender}") 
    # p1  = PassByReference("Female" , "Abhi") 
    # return p1 

p = PassByReference("Female" ,"aBHI") 
greet(p) 


def greet1(PassByReference) :
    print(f"Hello {PassByReference.name} and my gender is {PassByReference.gender}") 
    a  = PassByReference("male" , "ram") 
    return a 

p1 = PassByReference("Female" ,"aBHI") 
s =greet1(p1)  
print(s.name) 
print(s.gender)
