class Customer:
    def __init__(self , name , age , address): 
        self.name = name 
        self.age = age 
        self.address = address 

    def print_address(self) :
        print(self.address.city ,self.address.pin ,self.address.state )

class Address :
    def __init__(self, city,pin,state): 
        self.city = city 
        self.pin = pin 
        self.state = state
add = Address("Bhopal" , 23452 , "M.P.") 
cust = Customer("abhi" , 10 ,add) 
cust.print_address()