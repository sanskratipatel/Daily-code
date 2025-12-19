arr = [1,2,3,4,5,6,7] 
# arr = [8,7,6,5,4,3,2,1]
low = 0 
high = len(arr) -1
key = 7
if arr[0] <arr[1] :  
    while(low <= high) : 
        mid = low + (high -low) //2 
        if arr[mid] == key:
            print("Got key ar index ", mid) 
            break
        elif arr[mid] > key: 
            high = mid - 1 
        
        else: 
            low = mid +1 

elif arr[1] <arr[0] : 
    while(low <= high) :
        mid =  low + (high-low) //2 

        if arr[mid] == key:
            print("Key Found At index " , mid) 
            break

        elif arr[mid] > key: 
            low = mid +1  
        
        else: 
            high = mid -1 
    



