# K th Largeat Element  

import heapq
arr = [10, 2, 3, 4, 11, 7]
k = 3
min_heap = [] 
heapq.heapify(min_heap) 

for i in range(0 , len(arr)):
    heapq.heappush(min_heap,arr[i]) 
    if len(min_heap)> k:
        heapq.heappop(min_heap) 
print(min_heap) 
print("Third greater element ", min_heap[0])