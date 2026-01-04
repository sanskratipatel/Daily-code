nums = [0,1,2,3,5,6] 

sum = 0 
real_sum = 0
for i in range(0 , len(nums)+1) :
    if i !=  len(nums):
       sum = sum + nums[i]  
    real_sum = real_sum + i 
print(sum) 
print(real_sum -sum)