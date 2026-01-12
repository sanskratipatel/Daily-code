import numpy as np 

# Reshapes  (rows ,columns) Specify new Shapes
# If Dimensions match then we Reshape it  
# It does not create copy it affect original array 


arr = np.array([1,2,3,4,5,6]) 
res = arr.reshape(2,3) 
print(res) 


# Flatting :- Ravel and Flatten 
# When we convert Multidimensional Array into Flat  
# Ravel() -> it affect original array 
# Flatten () -> Create New Copy 

print(res.ravel()) 
print(res.flatten())