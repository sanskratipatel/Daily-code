nums =[11,12,15,18,2,5,6,8] 

low = 0 
high = len(nums)-1 
n = len(nums) 
midi = -1
is_sorted= False
while(low <=high) :
    
    if nums[low] <= nums[high] :
        midi = low
        is_sorted = True 
        break
    mid = low + (high-low)//2 
    prev = (mid-1 +n)%n 
    ne = (mid+1)%n 
    
    if nums[mid] < nums[prev] and nums[mid] < nums[ne] :  
        midi = mid 
        break
    if nums[low] <= nums[mid]: 
        low = mid +1 
    else:
        high = mid - 1 


def binary_search(low ,high, arr,key ) :  
    ans = -1
    while(low<=high) :
        mid = low + (high - low)//2
        if arr[mid] == key:
            ans = mid 
            break 
        elif arr[mid] > key :
            high = mid -1
        else:
            low = mid+1 
    return ans 
print(midi ,is_sorted)
key = 2 
if nums[midi] != key :
    left =binary_search ( 0 ,  midi-1 , nums ,2 ) 
    # print(left)
    right =binary_search (midi, n-1, nums ,2 ) 
    print(right)
    if right != -1 :
        print("ANS= ",right) 
    else :
        print("Ans = ",left)

else:
    print("Ans = ",midi) 

     

