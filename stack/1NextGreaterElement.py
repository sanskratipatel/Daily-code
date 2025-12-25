arr = [1,3,0,0,1,2,4] 

result = [-1] * len(arr) 

for i in range(0 , len(arr)) : 
    for j in range(i+1 , len(arr)) : 
        if arr[j] > arr[i] : 
            result[i] = arr[j]
            break 
print(result)