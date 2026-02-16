nums = [1,2,3,4,5,6,7] 

n= len(nums) 
r_time = 12 
k = r_time%n 

for i in range(0 , k) :
    e = nums.pop() 
    nums.insert(0, e) 
print(nums)