# Longest Substring Without Repeating Character 


str ="pwwkew" 
i = 0
j = 0 
my_dict = {} 
maxi = 0
while(j < len(str)) : 
    if str[j] in my_dict : 
        my_dict[str[j]] = my_dict[str[j]] +1 
    else:
        my_dict[str[j]] = 1 
    
    if len(my_dict) < (j-i+1) : 
        while len(my_dict) < (j-i+1) :  
            my_dict[str[i]] = my_dict[str[i]]-1 
            if my_dict[str[i]] == 0 : 
                del my_dict[str[i]] 
            i = i +1 
        j = j+1  
    
    elif len(my_dict)  == (j-i+1) : 
        if maxi < (j-i+1) : 
            maxi = j-i+1
        j = j+1 
print(maxi)

        

