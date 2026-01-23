class Person:
    def __init__(self):
        self.name = "Abhi" 
        self.place = "India" 

p = Person() 
# P is a reference Variable 
q =p 
print(q.name)
print(p.name) 
q.name = "Abc" 
print(q.name)
print(p.name) 