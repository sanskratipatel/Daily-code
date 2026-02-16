def merge_sorted_arr(arr1 , arr2) :
    result = [] 
    i = 0  
    m = len(arr1)
    j = 0  
    n =len(arr2) 
    while(i<m and j <n) :
        if arr1[i] <= arr2[j] :
            result.append(arr1[i]) 
            i = i+1 
        elif arr1[i] > arr2[j]:
            result.append(arr2[j]) 
            j = j+1 
    if i < m: 
        while(i<m) :
            result.append(arr1[i])
            i= i+1 
    if j<n:
        while(j<n):
            result.append(arr2[j])  
            j = j+1
    return result 


def merge_sort(arr) :
    if len(arr)<=1 :
        return arr 
    mid = len(arr)//2 
    left_arr =arr[: mid ] 
    right_arr=arr[mid : ] 
    left  = merge_sort(left_arr) 
    right = merge_sort(right_arr) 
    return merge_sorted_arr(left,right) 

arr1 = [5,4,6,2,5,7,4,1,1] 
ans = merge_sort(arr1)
print(ans)
    


