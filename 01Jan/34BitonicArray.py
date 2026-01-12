arr= [1,3,5,12,4,2] 


low = 0 
high = len(arr) -1 
n = len(arr)
ans =-1
e=0
while(low <= high) :
    mid = low + (high - low) //2 
    prev = (mid-1+n)%n 
    next = (mid+1)%n 
    
    if arr[mid] > arr[prev] and arr[mid] > arr[next] :
        e = mid
        ans = arr[mid] 
        break
    elif arr[mid] > arr[prev] : 
        low = mid + 1 
    else: 
        high = mid -1 

print(ans)
key = 4 
a1 = -1 
l1 = 0 
h1 = e-1 
while(l1 <= h1) :
    mid = l1 + (h1-l1)//2
    if arr[mid] == key:
        a1 = mid
        break 
    elif arr[mid] > key: 
        h1 = mid -1 
    else:
        l1 = mid +1 

l2 = e 
h2 = len(arr)-1 
a2 =-1
while(l2 <= h2) :
    mid = l2 + (h2-l2)//2
    if arr[mid] == key:
        a2 = mid 
        break 
    elif arr[mid] > key: 
        h2 = mid +1 
    else:
        l2 = mid -1 
if a2 != -1 :
    print(a2) 
elif a1 != -1 :
    print(a1)