# /Next greater to left 
# arr = [1,3,0,0,1,2,4] 
# arr = ar.reverse() 
arr = [1,3,2,4]
st = [] 
result =[]
for i in range(0 , len(arr)) : 
    if len(st) == 0 :
        result.append(-1) 
    elif len(st) != 0 and st[-1] <= arr[i] :  
        while len(st) != 0 and st[-1] <= arr[i]:  
            st.pop() 
        if len(st) == 0 :
            result.append(-1) 
        else: 
            result.append(st[-1]) 
    else :
         result.append(st[-1])
    st.append(arr[i]) 
result.reverse()
print(result)

 