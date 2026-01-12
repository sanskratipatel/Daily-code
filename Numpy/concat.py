import numpy as np 

arr1 = np.array([[1,2,3],[1,2,3]]) 
arr2 = np.array([[4,5,6],[6,5,4]])  
new_arr= np.concat([arr1,arr2]) 
print(new_arr)