arr = [5,-2,3,1,4,5,67] 

key = arr[-1] 

for i in range(len(arr)-2 , -1,-1) : 
    arr[i+1] = arr[i] 

arr[0] = key 
print(arr)