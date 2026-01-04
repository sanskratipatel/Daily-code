num1 = [1,2,3,4,5] 
num2 =[1,3,4,5,6,7,8,9] 

i = 0 
j = 0 
m = len(num1) 
n = len(num2) 
result =[]
while(i<m and j <n) :
    if num1[i] <= num2[j] :
        result.append(num1[i]) 
        i = i+1 
    elif num2[j] <= num1[i] :
        result.append(num2[j]) 
        j = j +1 

if i < m :
    while(i<m) :
        result.append(num1[i])  
        i = i+1

if j < n :
    while(j<n) :
        result.append(num2[j]) 
        j = j+1

print(result)