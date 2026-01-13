# Nearest Smallest to left 

arr= [4,5,2,10,8] 
ans = [] 
res = []
for i in range(len(arr)) : 
    if len(ans) == 0:
        res.append(-1) 
    elif len(ans) >0 and ans[-1] < arr[i] :
        res.append(ans[-1]) 
    elif len(ans) >0 and ans[-1] > arr[i] : 
        while(len(ans) >0 and ans[-1] >arr[i] ) :
            ans.pop() 
        if len(ans) == 0:
            res.append(-1) 
        else:
            res.append(ans[-1]) 
    ans.append(arr[i]) 

# res.reverse() 
print(res)
