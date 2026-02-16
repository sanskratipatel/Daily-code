# Sell and buy Stock 

prices = [7,2,1,5,6,4,8] 

max_profit = 0 

for i in range(0 , len(prices)) :
    for j in range(i+1 , len(prices)) :
        if prices[j]> prices[i] :  
            p = prices[j] - prices[i]
            max_profit = max(max_profit , p) 
print(max_profit)
