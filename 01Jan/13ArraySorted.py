nums = [3,5,6,7,8] 

asc = False 
desc = False 

if nums[0] < nums[1] :
    for i in range(0 , len(nums)-1):
        if nums[i] > nums[i+1] :
            asc = True 
            break
elif nums[0] > nums[1] :
    for i in range(0 , len(nums)-1):
        if nums[i] < nums[i+1] :
            desc = True 

if asc == False and desc == False :
    print("Array Is sorted ") 
else:
    print("Not Sorted")