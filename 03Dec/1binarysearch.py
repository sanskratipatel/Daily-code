arr = [1,2,3,4,5,6,7,8,9] 
key  = 6 

high = len(arr) -1 
low = 0 
while(low<=high):  
    mid = (low +high) //2
    if arr[mid] == key : 
        print("We find element at " ,mid) 
        break 
    elif (arr[mid] > key) : 
        high  = mid -1 
    else :
        low = mid +1 





