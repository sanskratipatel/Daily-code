nums = [5,54,2,4,2,43,6,57,34]
largest = float('-inf') 
sec_lar = float('-inf') 

for i in range(0 , len(nums)) :
    if nums[i] > largest: 
        sec_lar = largest
        largest = nums[i] 
    elif nums[i] > sec_lar and nums[i] != largest : 
        sec_lar = nums[i] 
print("Largest =",largest , "Second =",sec_lar)