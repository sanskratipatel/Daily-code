str1 = "IX" 

my_dict = {
         "I" :1 ,
         "V": 5,
         "X":10 ,
         "L":50 ,
         "C":100,
         "D":500 ,
         "M":1000
         }  
ans = 0  
invaid = 0
for i in range(0 , len(str1)) :  
    if i<len(str1)-1 and my_dict[str1[i] ]< my_dict[str1[i+1]]: 
        ans = ans - my_dict[str1[i]] 
    else:
        ans = ans + my_dict[str1[i]]
    
        
print(ans)