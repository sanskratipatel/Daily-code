arr = [1,2,3,4,5,6] 
k = 3 
sum = 0 
j = 0 
i = 0 
max_sum = float("-inf")
while(j < len(arr)) : 
    sum = sum + arr[j] 
    if (j-i+1) <k :
         j = j +1 
    elif (j-i+1) == k:  
        if max_sum < sum : 
              max_sum = sum   
        sum = sum -arr[i]
        j = j+1 
        i = i+1 

print(max_sum)
        
         
         