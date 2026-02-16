arr = [1,2,3,4,45,6,7] 
is_asc = True 
is_desc = True 
n = len(arr)
if arr[0] <arr[n-1] :  
    for i in range(0 , len(arr)) :
        if len(arr) != i+1 and arr[i] > arr[i+1] : 
            is_asc =False
            break 
if arr[0]>arr[n-1] : 
    for i in range(0 , len(arr)) :
        if len(arr) != i+1 and arr[i] < arr[i+1] : 
            is_desc =False
            break 
if is_asc == False or is_desc == False :
    print("Not Sorted")
else:
    print("Sorted")