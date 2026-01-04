a =[5,3,2,2,1,5,5,7,5,10] 
b =[10,111,1,9,5,67,2] 

hash_list =[0] * 11 
for i in range(0 , len(a)) : 
    hash_list[a[i]] = hash_list[a[i]] + 1 
print(hash_list)
for j in range(0 , len(b)) : 
    if b[j] >10 or b[j] < 0 : 
        print(0) 
    else:
        print(hash_list[b[j]] ) 

