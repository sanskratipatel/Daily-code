class Person:
    __counter = 0
    def __init__(self , name , age): 
        self.name = name
        self.age = age  
        self.cid = Person.__counter 
        Person.__counter = Person.__counter+1
        
    @staticmethod
    def getter() :
        return Person.__counter



        
p1 = Person('abhi' ,24 ) 
p2= Person("Me" ,100) 
p3 = Person("er" , 3) 

l1 =[p1,p2,p3] 
print(l1) 

for i in l1 :
    print(i.name , i.age ,i.cid) 

my_dict = {"p1" : p1, "p2" :p2 , "p3" :p3 } 

for key in my_dict :
    print(my_dict[key].age , my_dict[key].name,my_dict[key].cid) 
print(Person.getter()) 
