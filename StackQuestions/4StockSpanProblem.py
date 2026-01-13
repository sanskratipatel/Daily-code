arr = [100,80,60,70,60,75,85] 

res = [] 
ans =[]

for i in range (0 ,len(arr)) : 
    count = 1 
    
    if len(ans) ==0: 
        res.append(count) 
    elif len(ans) > 0 and arr[i]< ans[-1][0] :
        res.append(count) 
    elif  len(ans) > 0 and arr[i] > ans[-1][0] : 
        while(len(ans) > 0 and arr[i] > ans[-1][0] ) :
            count = count+ ans[-1][1]
            ans.pop() 
        if len(ans) ==0:
            res.append(count)  
        else:
            res.append(count)
   
    ans.append((arr[i], count))
print(res)


