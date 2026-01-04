nums = [4,1,6,7,3,4,5,2,8] 

def partitaion(arr,low,high) ->int: 
    i = low 
    j = high 
    pivot = arr[low]

    while(i<j) : 
        while i <= high-1 and arr[i] <= pivot  :  
            i = i+1
        while j>= low+1 and arr[j] > pivot :
            j = j-1 
        if i <j : 
            arr[i],arr[j] = arr[j] ,arr[i]   
    arr[low] ,arr[j] = arr[j] ,arr[low]
    return j

def quick_sort(arr,low,high) :
    if low <high :
        par_index = partitaion(arr,low,high) 
        quick_sort(arr,low ,par_index-1) 
        quick_sort(arr,par_index+1 ,high)

quick_sort(nums, 0 ,len(nums)-1) 
print(nums)