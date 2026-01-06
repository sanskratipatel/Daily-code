nums = [1,2,3,4,5,6,7] 

high = len(nums)-1 
low = 0 
key =5
while(low<=high) :
    mid = low + (high-low) //2 

    if key == nums[mid] :
        print("Element Find at index ",mid) 
        break
    elif key > nums[mid] : 
        low = mid +1 
    else :
        high = mid -1 
    
