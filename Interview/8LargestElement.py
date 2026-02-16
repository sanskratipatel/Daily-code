arr= [1,2,3,6,345,2,6,7,6] 

maxi = arr[0] 

for i in range(0 , len(arr)) :
    if maxi < arr[i] :
        maxi = arr[i] 

print(maxi)