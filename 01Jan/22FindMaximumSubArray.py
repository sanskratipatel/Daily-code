nums = [-2,1,-3,4,-1,2,1,-5.4] 
real_sum = 0 
sum = 0 

for i in range(0 , len(nums)) : 
    sum = 0 
    for j in range(i , len(nums)) :
        sum = sum + nums[j]
        if real_sum < sum : 
            real_sum = sum

print(real_sum) 


# Kadane Algorithm 


max_sum = float("-inf") 
total = 0
for i in range(0 , len(nums)) : 
    total = total + nums[i] 
    if max_sum <total:
        max_sum = total 
    if total < 0 :
        total = 0 
print(max_sum)
