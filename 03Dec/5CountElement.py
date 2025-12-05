# Count of a element in sorted array  

arr = [1,2,3,4,5,6,6,6,6,6,7,8,9] 

l = 0 
h = len(arr) -1 
key = 5 
 
l1 =-1 
while(l<=h):
    mid = l + (h-l) //2 
    if arr[mid] == key : 
        l1 = mid 
        h = mid -1 
    elif arr[mid] >key :
        h = mid -1 
    else:
        l = mid + 1 


l2 =0 
h1 = len(arr)-1 
l3 = -1
while(l2<=h1) : 
    mid = l2 + (h1 -l2)//2 

    if arr[mid] == key :  
        l3 = mid 
        l2 = mid +1 
    elif arr[mid] > key :
        h1 = mid -1 
    else:
        l2 = mid + 1 

print(l1 , l3)
occuerence = (l3 +1) - l1 
print(f"{occuerence} of elemet {key}")
    
