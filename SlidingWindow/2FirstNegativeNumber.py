# First Negative in every window size K 
arr = [12,-1,-7,8,-15,30,15,34] 

li = [] 
i = 0 
j = 0 
k =3
result = []
while(j< len(arr)) : 
    if arr[j] < 0 :
            li.append(arr[j]) 
    if (j-i+1 ) < k : 
        j = j +1 
    elif (j-i+1) == k : 
        if len(li) == 0 : 
             result.append(0) 
        else: 
            result.append(li[0])   
            if li[0] == arr[i] : 
                 li.pop(0)      
        i= i+1 
        j = j+1 
print(result)