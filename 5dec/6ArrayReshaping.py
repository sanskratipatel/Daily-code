import numpy as np 
arr = np.arange(12)
print("Orginal Array =",arr) 

reshaped = arr.reshape((4,3)) 
print(" \n Reshaped Array = ",reshaped) 


flattern = reshaped.flatten() 
print("flatten array = ", flattern)  


# It return Orginal array insead of copy of array 
reveled = reshaped.ravel() 
print("\n raveled Array = ",reveled )  


# Transpose 

transpose = reshaped.T
print("\n Transhposed Array = ",transpose )
