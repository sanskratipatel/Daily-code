import numpy as np 

# np.split() -> Split in equal part 
# np.hsplit() ->horizontal Splitting 
#  np.vsplit() -> Vertical Splitting  


arr = np.array([1,2,3,4]) 
print(np.split(arr,2)) 


arr1 = np.array([[1,2,3,4],[1,2,3,6]]) 
print(np.hsplit(arr1,2)) 
print(np.vsplit(arr1,2)) 