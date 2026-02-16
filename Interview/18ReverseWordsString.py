str1 = "the   sky   is    blue "  

arr = str1.split() 
ans = []
for i in range(len(arr)-1 , -1,-1) : 
    if arr[i] != " ":
       ans.append(arr[i]) 
 
ans = " ".join(ans) 
print(ans) 
