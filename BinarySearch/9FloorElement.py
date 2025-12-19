arr = [1,2,3,4,4,6,7,8,8,8,10,10,13,14]  

low = 0  
high = len(arr) 
key = 5

canditate = -1
while(low<=high) :
    mid = low +(high -low) //2 
    if arr[mid] == key : 
        print("find element at  =", mid , arr[mid]) 
    
    if arr[mid] <= key : 
        canditate = mid 
        low = mid +1 

    elif arr[mid] >= key: 
        high =  mid -1
        
print("Floor of that element is = " , canditate)