# Series :- It is 1D data that store datatype 
import pandas as pd 
import numpy as np 


country = ["India" , "USA","UK" ,"Nepal"] 
a = pd.Series(country) 
print(a) 

number =[12,14,15,26,42,65] 
b = pd.Series(number) 
print(b) 


# Custom iNDEX 

marks = [78,95,90,99] 
subject = ["English" , "Maths" , "SST" , "Hindi"]  
c = pd.Series(marks, index = subject ) 
print(c)
d  = pd.Series(marks, index = subject, name = "Mere number" ) 
print(d) 


# Series Using dict 

marks = { "hindi" :100 , "maths" : 90} 
e = pd.Series(marks , name = "Mere Marks") 
print(e)