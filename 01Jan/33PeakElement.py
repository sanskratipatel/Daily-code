arr = [5,10,20,15] 

low = 0 
high = len(arr) -1 
n = len(arr)
ans =-1
while(low <= high) :
    mid = low + (high - low) //2 
    prev = (mid-1+n)%n 
    next = (mid+1)%n 
    
    if arr[mid] > arr[prev] and arr[mid] > arr[next] :
        ans = arr[mid] 
        break
    elif arr[mid] > arr[prev] : 
        low = mid + 1 
    else: 
        high = mid -1 

print(ans)