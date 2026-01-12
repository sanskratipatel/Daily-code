# Next Alphabate 

# num = [1,2,3,5,6,7] 
# key =4
# high = len(num)-1 
# low = 0 
# ele =-1
# while(low <= high) :
#     mid = low + (high - low) //2 

#     if num[mid] == key:  
#         ele = mid 
#         break 
#     elif num[mid] > key : 
#         ele = key 
#         high = mid -1 
#     else:
#         low = mid +1 

# print(ele)
        
arr = ['a','b','c','d','h','i'] 

high = len(arr) -1 
low = 0 
ele = -1
key = 'd'
while(low <= high) :
    mid = low + (high - low) //2 
    if ord(arr[mid] )== ord(key) :  
        low = low +1 
    elif ord(arr[mid]) > ord(key) : 
        ele = mid
        high = mid -1 
    else:
        low = mid +1 

print(arr[ele])