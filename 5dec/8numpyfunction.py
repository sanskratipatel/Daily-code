import numpy as np 
a = np.arange(1,11) 
print("this is a = ", a ) 
# Arange with reshape 

b = np.arange(1,11).reshape(2,5)  
print("this is b = ", b )  

c = np.ones((3,4)) 
print("ones arraty  = ",c) 

d = np.zeros((3,4))
print("Zeros array = ",d) 

e = np.random.random((3,4)) 

print("Random Numbers = ",e)