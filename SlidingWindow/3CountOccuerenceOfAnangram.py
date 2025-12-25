str = "aabaabaa" 
k = "aaba" 

i = 0
j = 0 
my_dict = {} 

for o in range(0 , len(k)) : 
    if k[o] in my_dict:
        my_dict[k[o]] = my_dict[k[o]]+1 
    else : 
        my_dict[k[o]] = 1 


count = len(my_dict) 
print(count)
ans = 0
while(j < len(str)) : 
    if str[j] in my_dict : 
        my_dict[str[j]] =  my_dict[str[j]]-1 
        if my_dict[str[j]] == 0 : 
            count = count -1 
    
    if len(k) > (j-i+1): 
        j = j+1 
    elif len(k) == (j-i+1) : 
        if count == 0 :
            ans = ans + 1 
        if str[i] in my_dict : 
            my_dict[str[i]] =  my_dict[str[i]] + 1
            if my_dict[str[i]] == 1 :
                count = count +1 

        j =j +1
        i = i +1 

print(ans)