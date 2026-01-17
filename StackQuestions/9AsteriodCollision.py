nums = [4,7,1,1,2,-3,-7,17,15,-16,-18,-18] 

result = [] 

for i in range(0 , len(nums)) :
    if nums[i] >=0 :
        result.append(nums[i]) 
    elif nums[i] < 0 : 
        while(len(result) != 0 and  result[-1 ]>0 and abs(nums[i]) > result[-1 ] ) :
            result.pop() 

        if len(result)!=0 and result[-1] == abs(nums[i]): 
            result.pop()
        elif len(result) ==0 or result[-1] <0:
            result.append(nums[i]) 

print(result)