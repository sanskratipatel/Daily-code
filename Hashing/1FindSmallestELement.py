# Kth smallest Element If k=3 that means third smallest element 

import heapq 

arr = [10,2,2,3,4,11,8,8,7]  
max_heap = []
heapq.heapify(max_heap) 
k =3
print(arr) 
for i in range(0 , len(arr)) :  
    heapq.heappush(max_heap,-arr[i])
    if len(max_heap) > k : 
        heapq.heappop(max_heap)  
print(max_heap)

print("third smallest element is = ",-max_heap[0])