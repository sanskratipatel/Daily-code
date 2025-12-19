# Mininmum Difference ELement in a Sorted Array 


arr = [1,3,10,12,15] 

low = 0 
high = len(arr) - 1 
key = 8
res = -1
res1 = -1 
res2 = -1
while (low <= high) : 
    mid = low + (high - low) //2 

    if key == arr[mid] :  
        res = mid 
        break 

    elif arr[mid] > key :   
        res2 = mid 
        high = mid -1 
    else: 
        res1 = mid 
        low  = mid +1 



if res == -1 : 
    if (arr[res1] - key) > (arr[res2] - key) : 
        res = arr[res1] 
    elif (arr[res1]- key) < (arr[res2] - key) :  
        res = arr[res2]
print(res)