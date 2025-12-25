#  Number of times Sorted Array 
nums = [18,2,3,4,5,11,12,15] 
low = 0 
high = len(nums) -1 
n = len(nums)
while(low <= high) :
    if nums[low] <= nums[high]:
        print("Minimum index =", low)
        break
    mid = low + (high -low)//2
    next = (mid +1 )% n 
    prev = (mid +n -1) % n 

    if nums[mid] <= nums[next] and nums[mid] <= nums[prev]: 
        print("Mininmunm index is = " , mid) 
        break

    elif nums[low] <= nums[mid] : 
        low = mid +1 
    
    else : 
        high = mid -1 