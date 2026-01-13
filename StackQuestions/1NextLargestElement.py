# Next largest element to right  

arr = [1,3,0,0,1,2,4] 
result = []
for i in range(0 , len(arr)) :
    for j in range(i+1 , len(arr)) :
        if arr[j]>arr[i] : 
            result.append(arr[j]) 
            break 
print(result) 

arr = [1,3,0,0,1,2,4] 

ans = [] 
ans2 = []
for i in range( len(arr)-1,-1,-1) :
    if len(ans) == 0  :
        ans2.append(-1) 
    elif len(ans) >0 and ans[-1] > arr[i]:
        ans2.append(ans[-1]) 
    
    elif len(ans) >0 and ans[-1] < arr[i] :
        while(len(ans) >0 and ans[-1] <arr[i]) :
            ans.pop()
        if len(ans) ==0 :
            ans2.append(-1) 
        else :
            ans2.append(ans[-1]) 
    ans.append(arr[i]) 
ans2.reverse()

print(ans2)