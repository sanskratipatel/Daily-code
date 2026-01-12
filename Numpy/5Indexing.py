import numpy as np 

arr = np.array([1,2,3,4,5,6]) 

# Indexing
print(arr[0]) 
print(arr[2]) 


# Slicing  
# End exclude
print(arr[0:2])  


print(arr[0::2]) 

print(arr[::-1]) 


# Fancy Indexing 


print(arr[[0,3,5]])  

# Boolean Masking
print(arr[arr>5])