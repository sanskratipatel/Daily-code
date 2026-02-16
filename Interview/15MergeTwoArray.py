# Merge Array without Duplicate 


arr = [1,1,0,1,0,1,1,1,1,0,1,1,1,1,1] 

max_ones = 0 
maxi = 0 

for i in range(0 , len(arr)) : 
    if arr[i] ==1 :
        max_ones = max_ones+1 
    else:
       maxi =  max(maxi, max_ones) 
       max_ones = 0  
maxi = max(maxi, max_ones)
print(maxi)