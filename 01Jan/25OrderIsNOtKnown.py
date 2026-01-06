nums = [9,8,7,6,5,4,3,2,1]
high = len(nums) 
low = 0
key = 6
if nums[0] > nums[1] :  
    while(low <= high) :
        mid = low + (high -low) //2 

        if nums[mid] == key : 
            print("Elelent Found At index " , mid) 
            break
        elif nums[mid] > key :
            low= mid +1 
        else:
            high = mid -1 
else:
     while(low <= high) :
        mid = low + (high -low) //2 

        if nums[mid] == key : 
            print("element Found At index " , mid) 
            break
        elif nums[mid] < key :
            low= mid +1 
        else:
            high = mid -1 
