# Next Greater to left 


arr = [1,28,3,4,5,6] 
ans = [] 
res = []
for i in range(0 , len(arr)) : 

    if len(ans) == 0 : 
        res.append(-1) 
    elif len(ans) > 0 and ans[-1] > arr[i] :
        res.append(ans[-1] ) 
    elif len(ans) > 0 and arr[i] > ans[-1] :
        while( len(ans) > 0 and arr[i] > ans[-1]):
            ans.pop() 
        if len(ans) ==0 :
            res.append(-1 ) 
        else:
            res.append(ans[-1]) 
    ans.append(arr[i]) 
print(res)


 

