arr = [54,2,3456,86,3,57,65,8,4453] 
largest = float("-inf") 
sec_largest = float("-inf") 
for i in range(len(arr)) :
    if arr[i] > largest: 
        sec_largest = largest
        largest = arr[i] 
    elif arr[i] != largest and sec_largest <arr[i] :
        sec_largest = arr[i] 

print(largest) 
print(sec_largest)