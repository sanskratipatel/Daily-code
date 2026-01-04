nums = [1,2,3,4,6,7]  
n= len(nums)

nums[:] =[nums[-1]] + nums[0 :n-1]
print(nums) 

arr = [1,2,3,4,5,6] 
result = [] 
end = arr[0] 

for i in range(1 , len(arr)) : 
    result.append(arr[i])
result.append(end)