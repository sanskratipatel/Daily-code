from functools import reduce 

a = [1,2,3,4,5] 
d = reduce(lambda x ,y: x *y ,a)  
print(d)
def ans (x,y): 
    return x* y 

c = reduce(ans, a) 
print(c) 

