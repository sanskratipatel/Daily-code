nums = [1,2,3,4,5,6,7,8] 

low = 0 
high = len(nums) -1 
key = 7
found = False
while(low <= high): 
    mid = low + (high - low) //2 
    if key == nums[mid] : 
        print("We find element in " ,mid , " index") 
        found = True 
        break 
    elif key > nums[mid] : 
        low = mid +1 
    
    else: 
        high = mid -1 
    


