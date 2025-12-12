import numpy as np 
a = np.array([1,2,3,4] ,dtype = np.int32) 
print("dimension" ,a.ndim)
print("shape = ",a.shape)
print("size -",a.size)
print("item size = ",a.itemsize)
print("a = ", a) 

b = np.array([[1,2,3,4] , [7,8,9,0]]) 
print("dimension" ,b.ndim)
print("shape = ",b.shape)
print("size -",b.size)
print("item size = ",b.itemsize)
print("b = ", b) 

c = np.array([[[1,2,3] ,[4,5,6]],[[7,6,5],[4,3,2] ]])  
print("dimension",c.ndim) 
print("shape = ",c.shape)
print("size -",c.size)
print("item size = ",c.itemsize)
print("c = \n" , c)    

