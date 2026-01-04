arr = [112,54,2,6,3,6,34,1,5,7] 

for i in range(0 , len(arr)) : 
    for j in range(0 ,len(arr)-1 ) :
        if arr[j] > arr[j+1] :
            arr[j] , arr[j+1] = arr[j+1] , arr[j] 
    
print(arr)