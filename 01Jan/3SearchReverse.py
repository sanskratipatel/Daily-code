arr = [8,7,6,5,4,3,2,1]

high = len(arr) 
low = 0 
key = 5
while(low<= high) :
    mid = low +(high-low)//2 

    if key == arr[mid]:
        print("Element found at ",mid) 
        break 
    elif key > arr[mid] :
        high = mid -1 
    else :
        low = mid +1 
    
    