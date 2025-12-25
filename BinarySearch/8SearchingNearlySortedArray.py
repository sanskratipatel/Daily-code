arr = [5,20,10,30,40,50] 

low = 0 
n = len(arr)
high = len(arr) -1 
key  =50

while(low<=high) :
    mid = low +(high -low) //2 
    if arr[mid] == key  : 
        print("Find  ELement  at ", mid)  
        break
    if (mid +1 != n and  arr[mid+1] ==key ) : 
        print("Find  ELement  at ", mid+1)  
        break
    if ( mid != 0 and arr[mid-1] == key): 
        print("Find  ELement  at ", mid-1)  
        break
    elif arr[mid] > key:  
        high  = mid -2 
    else:
        low = mid +2

 

    