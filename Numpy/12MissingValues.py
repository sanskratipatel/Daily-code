import numpy as np 

# isNan : - Detect Missing Value 
# nan_to_num() :- Convert nan to number 
# np.isinf () :-  

# Does We compare Nan Value : - NOOOOOO (using == no ) 
arr = np.array([1,2,np.nan,4,np.nan, 6]) 
print(np.isnan(arr)) 
# print(np.nan == np.nan)  We cannot compare it directly 

# np.nana_to_num default vlaue = 0 

cleaned_arr = np.nan_to_num(arr,nan=100) 
print(cleaned_arr) 

# np.isinf() :- Handling infinte Values 

arr1 = np.array([1,2,np.inf, 4 ,-np.inf]) 
print(arr1) 
cleaned_arr1 = np.nan_to_num(arr1,posinf =1000,neginf=-100) 
print(cleaned_arr1)