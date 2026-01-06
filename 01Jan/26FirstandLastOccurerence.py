nums = [2,4,10,10,10,18,20] 
# Lower Index
low = 0 
high = len(nums) 
key = 10
ans = -1
while(low <= high) :
    mid = low +(high-low)//2 

    if nums[mid]==key :
        ans = mid
        high = mid-1 
    elif nums[mid] > key:
        high = mid-1 
    else:
        low = mid +1 

print("Ans Find" ,ans)

ans2 =-1 

l = 0 
h = len(nums) 
# For High Occuerence
while(l<=h) :
    mid = l + (h - l)//2 
    if nums[mid] == key :
        ans2 = mid
        l = mid +1  
    elif nums[mid] > key :
        h= mid-1 
    else:
        l = mid+1 
print(ans2 , "Last Occuerence")