arr = [3,5,6,1,6,3,5,8,4] 

for i in range(0 , len(arr)) :
    for j in range(i+1, len(arr)) :
        if arr[i] > arr[j]:
            arr[i] , arr[j] = arr[j] , arr[i] 
print(arr)