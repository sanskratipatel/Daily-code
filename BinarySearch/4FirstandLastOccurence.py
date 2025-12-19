# Finding Any Element First Occurenece 


arr = [ 1,2,3,4,4,4,4,5,6,7,8] 

low = 0 
high = len(arr) - 1 
key = 4
result = -1
while(low <= high) : 
    mid = low + (high - low) //2 

    if key == arr[mid] : 
        result = mid
        high =  mid -1 
    
    elif key > arr[mid] : 
        low = mid +1 
    else: 
        high = mid -1 

print("We find Result = ",result) 


arr1 = [ 1,2,3,4,4,4,4,5,6,7,8] 

low1 = 0 
high1 = len(arr1) -1 
res = -1 

while(low1<= high1) : 
    mid = low1 + (high1 - low1) //2 

    if key == arr1[mid] : 
        res = mid 
        low1 = mid +1 

    elif key> arr1[mid]: 
        low1 = mid +1 
    else : 
        high1 = mid -1 

print(" We fIND rESULT HIGH INDEX = ",res)