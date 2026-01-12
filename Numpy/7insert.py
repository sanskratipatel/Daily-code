import numpy as np 
# Np.insert (array,Index, Value, asix=None ) 
# Array -> Original Array 
# Index
# Value
# Axis
# Axis = 0 , row-wise 
# 1 Column Wise
arr = np.array([1,2,3,4,6,7,8]) 
new_arr = np.insert(arr,3,100, 0)  

print(new_arr)
arr2 = np.array([[1,2,3] ,[2,3,5],[2,3,5]]) 
new = np.insert(arr2,0,[6,7,8], axis = 1 ) 
print(new)

new1 = np.insert(arr2,0,[6,7,8], axis = 0 )  
print(new1)

new3 = np.insert(arr2,0,[6,7,8], axis = None )  
print(new3) 


# Append  
arr3 = np.array([[1,2,3],[2,3,4],[5,6,7]])  
print(arr3) 
new_arr3 = np.append(arr3,[6,7,8] )