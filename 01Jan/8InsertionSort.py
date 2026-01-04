nums = [3,5,4,6,2,6,2,7,8] 

for i in range(0 , len(nums)) :
    key = nums[i] 
    j = i-1

    while(j>0 and nums[j] > key) :
        nums[j+1] = nums[j] 
        j = j-1 
    nums[j+1] = key 