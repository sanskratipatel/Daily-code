# Find subarray with maximum sum 

arr = [4,1,1,1,3,5]  
target = 5 
j = 0 
i = 0 
sum = 0 
maxi = 0
while(j < len(arr)) : 
    if sum < target : 
        sum = sum +arr[j]
        j = j+1 

    elif sum == target :  
        if (j - i) > maxi :  
            maxi = j-i 
        sum = sum - arr[i]
        i = i+1
    elif sum > target : 
        while(sum > target) :  
            sum = sum -arr[i] 
            i = i+1  
       
print(maxi)



