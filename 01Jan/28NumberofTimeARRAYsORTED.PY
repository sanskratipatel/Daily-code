nums = [11,12,15,18,2,5,6,8] 
low = 0 
high = len(nums) -1 
n = len(nums)
while(low <= high) :
    mid = low + (high -low) //2 
    ne = (mid + 1 ) %n 
    prev = (mid+n-1)%n 
    if nums[low] <= nums[high]:
        print("Minimum Element Index =", low)
        break
    if nums[mid] <= nums[prev] and nums[mid] <= nums[ne]:
        print("Mininmum ELement = ", mid) 
        break
    if nums[low] <= nums[mid] : 
        low = mid+1 
    else:
        high = mid -1 


