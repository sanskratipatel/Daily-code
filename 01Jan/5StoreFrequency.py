nums =[2,3,4,2,4,2,5,6,3,6]  

my_dict = {} 

for i in range(0 , len(nums)) : 
    if nums[i] in my_dict : 
        my_dict[nums[i]] = my_dict[nums[i]] +1 
    else:
        my_dict[nums[i]] = 1 

print(my_dict)