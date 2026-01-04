nums = [1,2,3,4,5,6,7,8] 

key = 9
k = key % len(nums)
print(k)
for i in range(0 , k) : 
    e= nums.pop() 
    nums.insert(0,e) 
print(nums)