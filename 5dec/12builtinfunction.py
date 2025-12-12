import numpy as np 
a1 = np.random.random((3,3) ) 
a1 =  np.round(a1 * 100) 
a1 = a1.astype(int)     
print(a1) 
print() 
print(np.min(a1)) 
print() 
print(np.max(a1)) 
print() 
print(np.sum(a1)) 
print() 
print(np.prod(a1)) 

# row minimum 
#  0 -> column  and 1 ->row 
# Max elsement of row 
print(np.max(a1 ,axis =1))
# Max elsement of column
print(np.max(a1 ,axis =0))
print(np.min(a1 ,axis =1))
print(np.min(a1 ,axis =0))
print(np.sum(a1 ,axis =1))
print(np.sum(a1 ,axis =0))
print(np.prod(a1 ,axis =1))
print(np.prod(a1 ,axis =0))   


# Means  all means or row or column wise also 
print(np.mean(a1))
print(np.mean(a1,axis = 1))
print(np.mean(a1,axis = 0)) 

# median  all means or row or column wise also  

print(np.median(a1))
print(np.median(a1,axis = 1))
print(np.median(a1,axis = 0))  


# dot product 

a2 = np.arange(12).reshape(3,4) 
a3 = np.arange(12,24).reshape(4,3) 
print(a2) 
print() 
print(a3) 
print()

print(np.dot(a2,a3))

# log and exponents 
print(np.log(a1)) 
print() 
print(np.exp(a1)) 
print()  

# Round Floor ceil 

a4 = np.random.random((2,3)) *100 
print(a4) 
print()
print(np.round(a4)) 
print()
print(np.ceil(a4)) 
print()
print(np.floor(a4))