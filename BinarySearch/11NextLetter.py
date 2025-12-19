# Next Letter Problem 

arr =['a','b' ,'c','f','g','h','i']  

low = 0 
high = len(arr) -1 
res = -1
key = 'f'
while(low<=high ) : 
    mid =  low + (high -low) //2  
    
    
    if arr[mid] > key:  
        res = mid 
        high = mid -1
    else :  
        low = mid + 1

   
print("res = ",res , arr[res])