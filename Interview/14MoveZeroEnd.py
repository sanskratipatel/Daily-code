nums =[1,2,3,0,4,0,5,0,6] 
temp = []
for i in range(0 , len(nums)) :
    if nums[i] != 0 :
        temp.append(nums[i]) 

for j in range(0 , len(temp)) :
    nums[j] = temp[j] 

for i in range(len(temp) , len(nums)) :
    nums[i] = 0 

print(nums)