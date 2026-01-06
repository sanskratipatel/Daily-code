arr = [1,2,3,4,6,7,8,9] 
# floor element
low = 0
high = len(arr) -1 
key = 5
res = -1
while(low<=high):
    mid = low + (high -low) //2 
    if arr[mid] == key : 
        res = mid
        print("Data find on index", mid) 
        break 
    elif arr[mid] > key : 
        high = mid -1 
    else:
        res = mid
        low= mid +1  

print(res)


# ceil found greater elelemnt 
arr = [1,2,3,4,6,7,8,9] 

low = 0
high = len(arr) -1 
key = 5
while(low<=high):
    mid = low + (high -low) //2 

    if arr[mid] == key : 
        res = mid
        print("Data find on index", mid) 
        break 
    elif arr[mid] > key : 
        res = mid
        high = mid -1 
    else:
        
        low= mid +1  

print(res)