num = "624601" 
ans = ""
for i in range(len(num)-1, -1,-1) : 
    if int(num[i]) == 1 or int(num[i]) %2 != 0 :  
        ans = num[:i+1]
        break 


if ans == "" : 
    print("All even no")
print(ans)
