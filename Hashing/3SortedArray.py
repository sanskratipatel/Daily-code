import heapq 

arr = [6,5,3,2,8,10,9] 

result = [] 

min_heap = [] 
heapq.heapify(min_heap) 
k = 3 

for i in range(0 , len(arr)) : 
    heapq.heappush(min_heap, arr[i])  
    if len(min_heap) >k : 
        result.append(heapq.heappop(min_heap)) 
for j in range(0 , len(min_heap)) : 
    result.append(heapq.heappop(min_heap))  

print(result)



