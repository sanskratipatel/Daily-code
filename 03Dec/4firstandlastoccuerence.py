# Fisrt and last occuerence of element 

# 1.First Occuerence 

arr = [1,2,3,4,5,5,5,5,5,7,8,9]  
key = 5 
low = 0 
high = len(arr) - 1 
find = -1
while(low <= high) :
    mid = low+ (high -low) //2 

    if arr[mid] == key:
        find = mid 
        high = mid -1  

    elif arr[mid] > key: 
        high = mid -1
    else:
        low = mid+1 
print(find , "last occuerence") 


# lAst Occuerence 
h = len(arr) - 1
l = 0 
f1 = -1
while(l <= h) :
    mid = l + (h -l) //2 
    if arr[mid] == key :
        f1 = mid 
        l = mid +1 
    elif arr[mid] > key:
        h = mid -1 
    else :
        l = mid +1 
print(f1)
