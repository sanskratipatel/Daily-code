# arr = [1,3,0,0,1,2,4] 

# res = [] 
# st = [] 


# for i in range(len(arr)-1 , -1 , -1) : 
#     if len(st) == 0 :
#         res.append(-1) 
#     elif len(st) != 0 and st[-1] < arr[i] :
#         while(len(st) >0 and st[-1] < arr[i]):
#             st.pop() 
#         if len(st) == 0 :
#           res.append(-1)  
#         else :
#           res.append(st[-1])    
#     else : 
#        res.append(st[-1]) 

    
#     st.append(arr[i]) 

# print(res.reverse())
# print(res)
    
arr = [1,3,0,0,1,2,4]

res = []
st = []

for i in range(len(arr)-1, -1, -1):
    if len(st) == 0:
        res.append(-1)

    elif st[-1] <= arr[i]:
        while (len(st) != 0) and (st[-1] <= arr[i]):
            st.pop()

        if len(st) == 0:
            res.append(-1)
        else:
            res.append(st[-1])

    else:
        res.append(st[-1])

    st.append(arr[i])

res.reverse()
print(res)
