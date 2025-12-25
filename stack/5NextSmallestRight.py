# NeXt Smallest to Left  


arr = [4,5,2,10,8] 

result = [] 
st = [] 

for i in range(0 , len(arr)) : 
    if len(st) == 0 :
        result.append(-1) 
    elif len(st) != 0 and st[-1] >= arr[i] :
        while (len(st) != 0) and (st[-1] >= arr[i]) : 
            st.pop() 
        if len(st) == 0:
            result.append(-1) 
        else:
            result.append(st[-1]) 
    else:
        result.append(st[-1] ) 

    st.append(arr[i])
print(result)