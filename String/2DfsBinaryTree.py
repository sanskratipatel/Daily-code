s= "the sky is blue" 
arr = s.split(" ") 
print(arr) 
rev = ""
ans = []
for i in range(len(arr)-1,-1,-1) : 
    rev = rev + " " + arr[i]  
    ans.append(arr[i]) 

result = " ".join(ans) 
print(result)
print(rev.strip())
