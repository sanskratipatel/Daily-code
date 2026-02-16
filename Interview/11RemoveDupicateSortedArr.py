nums = [1,2,2,3,4,5,6,7,7,3] 

my_dict = {} 
for i in range(0 , len(nums)) :
    if nums[i] not in my_dict:
        my_dict[nums[i]] = 0  
i = 0
for key in my_dict : 
    nums[i]  = key
    i = i+1 
print(i)
   
print(nums)