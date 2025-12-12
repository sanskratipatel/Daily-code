import numpy as np

py_list = [1,2,3,4,5] 
print("Multiple by 2 = ", py_list*2) 
# Multiple by 2 =  [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
np_arr = np.array([1,2,3,4,5]) 
print("Python array = ",np_arr *2 ) 
# Python array =  [ 2  4  6  8 10] 


import time 

start = time.time() 

py_list = [i*2 for i in range(10000)]  
print("Time taken list = ", time.time() - start) 

start1 = time.time()
np_list = np.arange(1,100000) *2 

print("Time taken array = ", time.time() - start1)