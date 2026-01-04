
from typing import List


def merge_two_array(arr1 :List[int] ,arr2 :List[int]) ->list:
    result=[]  

    i = 0
    j = 0 
    m = len(arr1) 
    n = len(arr2) 

    while(i< m and j <n) : 
        if arr1[i] < arr2[j]: 
            result.append(arr1[i])  
            i = i+1
        else: 
            result.append(arr2[j]) 
            j = j+1 
        
    if i <m : 
        while(i<m) : 
            result.append(arr1[i]) 
            i = i+1 
    if j<n:
        while(j<n) :
            result.append(arr2[j]) 
            j = j+1 
    return result


def merging_sorting(arr: List[int]) ->list :
    if len(arr) <=1 :
        return arr 
    mid = len(arr) //2  
    left_arr = arr[:mid] 
    right_arr =arr[mid:] 
    left_half = merging_sorting(left_arr) 
    right_half = merging_sorting(right_arr) 

    return merge_two_array(left_half,right_half)

nums = [3,4,2,1,5,3,4,67,3,7,42] 
ans = merging_sorting(nums)
print(ans)