arr = [1,2,3,4,5,6] 

low = 0 
high = len(arr) -1 
key =5 
if arr[low] > arr[high] : 
    while(low <= high) : 
        mid = low + (high-low)//2 
        if arr[mid] == key :
             print(f"Find Element at {mid}")
             break
        elif arr[mid] > key:
            low = mid +1 
        else:
            high = mid-1 
elif arr[low] < arr[high]  : 
    while(low <= high) :
        mid = low + (high -low)//2 

        if arr[mid] == key:
            print(f"Find element at place {mid}") 
            break 
        elif arr[mid] > key: 
            high = mid -1 
        else : 
            low = mid +1 

