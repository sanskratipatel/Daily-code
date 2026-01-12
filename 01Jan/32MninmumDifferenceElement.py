arr = [1,3,8,10,18] 
key =12 

high = len(arr)-1 
low = 0 
mini = -1
e1 = -1
while(low<= high) :
    mid = low + (high -low) //2 

    if arr[mid] == key: 
        mini = arr[mid]  
        break
    elif arr[mid] > key :
        e1 = mid
        mini = arr[mid] 
        high = mid -1 
    else:
        low = mid + 1 
maxi = -1 
e2 = -1
if mini != key : 
    l = 0 
    h =len(arr) -1 
   
    while(l<= h) :
        mid = l + (h -l) //2 
        if arr[mid] == key: 
            maxi = arr[mid] 
            break
        elif arr[mid] > key :
            
            h = mid -1 
        else:
            maxi = arr[mid] 
            e2 = mid
            l = mid + 1  
print(mini , maxi)
diff = abs(key - mini)
dif  = abs(key - maxi)

if diff < dif : 
    print("Ans is ",mini, e1)
   
elif dif < diff:
     print("Ans is " ,maxi,e2) 
   