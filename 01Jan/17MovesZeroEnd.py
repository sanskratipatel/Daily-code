nums = [1,0,2,4,3,0,0,3,5,1] 

result = [0] * len(nums)
id =0
for i in range(0 , len(nums)) :
    if nums[i] !=0 :
        result[id]= nums[i] 
        id = id +1 

for j in range(0 , len(result)) :
    nums[j] = result[j] 
print(nums)