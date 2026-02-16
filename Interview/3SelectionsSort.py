arr = [2,4,2,3,6,6,7,4,2] 

for i in range(0 , len(arr)) :
    min_index = i
    for j in range(i+1, len(arr)) : 
        if arr[j] <arr[min_index]: 
             min_index = j
    arr[min_index] ,arr[i] = arr[i] ,arr[min_index] 

print(arr) 