arr = [1,2,3,4,5,8,9,10] 

low =  0 
high = len(arr) -1 
key = 5
ele = -1
while(low<=high) : 
    mid = low+ (high-low) //2 

    if arr[mid] == key :  
        print("Find element at index" , mid) 
        break
    if arr[mid] >key: 
        ele = mid 
        high = mid -1  
    elif arr[mid] < key : 
        low = mid +1 
    
print("Ceil of element " , ele)
