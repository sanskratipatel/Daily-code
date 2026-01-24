class Parent:
    def __init__(self):
        self.name = 'Abhi' 
    def login(self):
        print("Login Sucessfully") 

class Child(Parent): 
    def __init__(self):
        self.rollno = 12 
    def enroll(self) :
        print("Enroll SuccessFully") 
 
c1 = Child() 
print(c1.enroll()) 
c1.login() 
print(c1.rollno)