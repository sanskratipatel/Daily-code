arr = [5,10,30,20,40] 
low = 0 
high = len(arr)-1 
n = len(arr)
key = 10
res = -1
while(low<=high) :
    mid = low + (high -low)//2 
    prev = (mid-1+n)%n 
    ne = (mid+1)%n 
    if arr[mid] == key :
        res = mid
        break
    if arr[prev] == key :
        res = prev
        break
    if arr[ne] == key : 
        res = ne 
        break 
    if arr[mid] >key :
        high = mid-2
    else:
        low =mid +2

print(res)