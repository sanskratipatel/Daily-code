n = 153 

n1  =n   
arm = n
ans = 0
count = 0  

while(n>0) : 
    count = count +1 
    n = n//10 

while(n1>0) :  
    ans = ans  + (n1%10) ** count
    n1 = n1//10
if ans == arm:
    print("Armstrong" ,ans) 
else:
    print("Nooooooo", ans)