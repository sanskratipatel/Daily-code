import random
class Atm() :
    def __init__(self):
        self.pin = "" 
        self.__balance = 0   
        self.otp = "" 
        self.max_try = 0
        # self.menu()
    
    def menu(self) :
        user_input= input( """ 
        Hi How Are You 
        1. Press 1 to create Pin
        2. Press 2 to change pin
        3. Press 3 to check Pin 
        4. Press 4 to withdraw
        5. Anything else to exit                    
    """)   
    
        if user_input =='1' :
            self.create_pin() 
        elif user_input=='2':
            self.change_pin() 
        elif user_input =='3' :
            self.check_balance() 
        elif user_input == '4' :
            self.withdraw_money() 
        else:
            exit() 

    def create_pin(self) :
        user_pin = input("Enter your pin :") 
        self.pin = user_pin
        
        user_balance = input("Enter your balance ") 
        self.__balance = user_balance 
        print("Pin Create Successfully")
        # self.menu()
    
    def set_new_pin(self) :
        new_pin = input ("Enter new Pin ")  
        self.pin = new_pin  
        print("Pin change successfully") 
        self.menu()

    def change_pin(self) :
        user_new_pin = input("Enter Your Pin ") 
        if user_new_pin == self.pin : 
            self.set_new_pin()
            
        else:
            print("Please Enter Correct Pin or Press 1 for Send Otp to your Registerd Number  ") 
            self.otp_func()  

    def otp_func(self  ) :   
       
        for attempt in range(3) :
            if self.max_try <= 3 : 
                user_input = input("Enter input ") 
                if user_input == "1" : 
                    self.otp = random.randint(1, 10000)
                    print("Otp Send to your Phone = ",self.otp )  
                otp_input = int(input("Enter Otp Please = ")) 
                if otp_input == self.otp :
                    self.set_new_pin() 
                    return
            else:
                print(f"Incorrect OTP. Attempts left: {2 - attempt}")
        print("Your Limit Exceed Try Again Later") 
        self.menu()
        
    def check_balance(self) :
        user_input = input("Enter Your Pin :") 
        if user_input == self.pin :
            print("Your Current Balance is " , self.__balance) 
        else:
            print("Incorrect Pin. Please Enter Correct Pin")  
            

    def withdraw_money(self) :
        user_pin = input("Enter Your Pin")
        if user_pin == self.pin : 
            amount = int(input("Enter Amount :")) 
            if amount <= self.__balance :
                self.__balance = self.__balance - amount 
                print("Money Withdraw Successfully") 
               
            else: 
                print("Insufficent Balance") 
        else:
            print("Incorrect Pin")
        
        self.menu() 

s1 = Atm() 
s1.create_pin()
s1.__balance= "str" 
s1.withdraw_money()


   

        

     
