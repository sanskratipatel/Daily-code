# Search reverse sorted array 

arr = [8,7,6,5,4,3,2,1] 
key =2
low = 0 
high = len(arr) -1 

while(low <= high) : 
    mid =low + (high-low)//2 

    if arr[mid] == key :
        print(f"Get element at place {mid}") 
        break 
    elif arr[mid] > key:
        low = mid+1 
    else : 
        high = mid -1 

