price = [7,2,1,5,6,4,8] 

maxi =0 

for i in range(0 , len(price)) :
    for j in range(i+1 , len(price)) :  
        if price[j] >price[i] :
            p = price[j] - price[i] 
            maxi = max(maxi, p) 
    


print(maxi)