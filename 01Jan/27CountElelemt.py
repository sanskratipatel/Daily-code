nums = [1,2,3,4,5,6,7,8,9] 


low = 0 
high = len(nums) -1
key = 5
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
h = len(nums) -1
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


print("Count of element = ", (ans2-ans)+1)