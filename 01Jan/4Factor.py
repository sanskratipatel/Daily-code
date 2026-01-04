num = 20 
result = [] 
i =2
while(i< (20//2)+1):  
    if num%i ==0 :
        result.append(i) 
    i=i+1

result.append(num)
print(result)

