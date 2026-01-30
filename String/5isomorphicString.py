s = "BACD"
t = "BABA" 
if len(s) == len(t) :
    my_dict1 = {} 
    my_dict2 = {} 

    for i in range(0 , len(s)) :
        char_s = s[i] 
        char_t = t[i] 
        if char_s in my_dict1 :
            if char_s != char_t : 
                print("Nott1")  
                exit() 
        else:
            my_dict1[char_s] = char_t 

        if char_t in my_dict2 :
            if char_s != char_t : 
                print("Nott")  
                exit() 
        else:
            my_dict2[char_t] = char_s 
print("Yayyyyyyy")