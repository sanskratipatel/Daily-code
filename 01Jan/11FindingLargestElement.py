nums = [-5,-4,-2,-6,-31,-6,-12,-53] 

largest = nums[0] 

for i in range(0 , len(nums)) :
    if nums[i] > largest : 
        largest = nums[i] 
print(largest)