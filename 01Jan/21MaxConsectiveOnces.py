num = [1,1,0,1,0,1,1,1,1,0,1,1] 

ans = 0 
real_ans = 0 
for i in range(0 , len(num)) : 

    if num[i] == 1 :
        ans = ans +1 
    else :
        if real_ans < ans :
            real_ans = ans 
        ans = 0 

if real_ans < ans :
        real_ans = ans 
print(real_ans)