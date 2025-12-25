import pandas as pd 
import numpy as np 


marks = [78,95,90,99] 
subject = ["English" , "Maths" , "SST" , "Hindi"]  
c = pd.Series(marks, index = subject, name = "112" ) 
print(c)
print(c.size) 


print(c.dtype) 
print(c.name) 
# All item is unique then true 

print(c.is_unique) 
d = pd.Series([1,2,3,4,2]).is_unique 
print(d)
# All index
print(c.index)  
# All marks 
print(c.values)

