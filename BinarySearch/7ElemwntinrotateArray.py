arr = [11,12,15,18,2,5,6,8] 
n = len(arr)
high = n -1 
low = 0 
smaller = -1
while(low<= high) :
    mid =  low + (high -low) //2 
    next = (mid +1 ) %n 
    prev = (mid+n-1) %n 

    if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:  
        smaller = mid 
    elif arr[low] <= arr[mid] : 
          low =  mid +1 
    else : 
         high  = mid -1 

key =15
l1 = 0  
h1= smaller -1 
find1 = -1
while (l1 <=smaller) : 
    mid = (l1+h1) //2  
    if arr[mid] == arr[key] : 
         find1 =  mid 
         break
    elif arr[mid] > key: 
         h1 = mid -1 
    else:
         l1 = mid +1 


l2 = smaller 
h2  = n-1
find2 = -1
while (l2 <=h2) : 
    mid = (l2+h2) //2  
    if arr[mid] == key : 
         find2 =  mid 
         break
    elif arr[mid] > key: 
         h2 = mid -1 
    else:
         l2 = mid +1 

print("find elsement in find1 ", find1 , "find elsement at find2 = ", find2)