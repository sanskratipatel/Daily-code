# Maximum SubArray of Size K 

arr = [5,3,2,5,1,4,7,4,2] 

k = 3 
i = 0 
j = 0 
res = [] 
 
m = []
while(j < len(arr)) :
    
    while len(m) !=0 and m[-1] < arr[j] :
        m.pop() 
    m.append(arr[j])
    if k > (j-i+1) : 
        j = j+1 
    elif  k == (j-i+1): 
        res.append(m[0])
        if arr[i] == m[0] : 
            m.pop(0) 

        j= j+1
        i = i+1 

print(res)
