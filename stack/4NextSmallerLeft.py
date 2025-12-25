# Next smaller to the right 
arr = [4,5,2,10,8] 
result = [] 
st = [] 

for i in range(len(arr)-1, -1, -1) :
    if len(st) == 0 :
        result.append(-1) 
    elif len(st) != 0 and arr[i] <= st[-1] : 
        while (len(st) != 0) and (arr[i] <= st[-1]): 
            st.pop() 
        if len(st)==0 :
            result.append(-1) 
        else:
            result.append(st[-1] ) 
    else:
        result.append(st[-1]) 
    st.append(arr[i]) 
print(result) 

result.reverse() 
print(result)