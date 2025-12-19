arr = [8,7,6,5,4,3,2,1] 

high = len(arr) -1 
low = 0 
key = 4

while(low <= high) : 
    mid = low + (high - low) //2 

    if arr[mid] == key :  
        print("Data find on ", mid) 
        break

    elif arr[mid] > key:  
        low = mid +1 
    else : 
        high = mid -1 

 