def my_deco(func) :
    def wrapper() :
        print("********************") 
        func() 
        print("********************") 
    return wrapper 
@my_deco
def hello() :
    print("hello") 

a =hello()
@my_deco
def mee():
    print("logic") 
d = mee()  

import time
def excute_time(func) :
    def wrapper(*args , **kwargs) :
        start = time.time() 
        func(*args , **kwargs) 
        print(f"total time it take {time.time() - start}")  
    return wrapper 

#
# def greet() :
#     print("Hello World") 
#     time.sleep(3)  

@excute_time
def square(a) : 
    time.sleep(1) 
    print(a*a)

square(4)

@excute_time
def data(my_dcit) : 
    li = []
    for key in my_dcit:
        li.append(key) 
    print(li) 


my_dict = {"avbh" :1 , "e" :4} 
data(my_dcit=my_dict)