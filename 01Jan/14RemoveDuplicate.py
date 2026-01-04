nums = [1,1,1,21,5,12,1,3,4,3,5,2,5] 

ans = set(nums) 
print(ans) 
my_dict = {}
print(nums)
for i in range(0 , len(nums)) :   
    if nums[i] not in my_dict:
        my_dict[nums[i]] = 1 

j = 0
for key in my_dict : 
    nums[j] = key 
    j = j+1 
print(nums)
print(j)
print(len(my_dict))