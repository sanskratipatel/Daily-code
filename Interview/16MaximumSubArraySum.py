arr = [-2,1,-3,4,-1,2,1,-5,4] 
maxi = float("-inf") 
for i in range(0 , len(arr)) :
    total = 0 
    for j in range(i , len(arr)) :
        total = total + arr[j] 
        maxi = max(total , maxi) 

print(maxi) 

maxi1 = float("-inf") 
total1= 0


for i in range(0 , len(arr) ): 
    total1 = total1 +arr[i] 
    maxi1 = max(maxi1 , total1) 
    if total1 <0 :
        total1 = 0 
print(maxi1)