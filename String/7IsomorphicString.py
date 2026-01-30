s= "anagrom"
d = "nagaram" 

find = True
if len(s) == len(d):
    my_dict = {}  
    for i in range(0 , len(s)) :
        if s[i] not in my_dict:
           my_dict[s[i]] = 1 
        else: 
             my_dict[s[i]] =  my_dict[s[i]] +1 
    
    for  j in range(0 , len(d)):
        if d[j] in my_dict and  my_dict[d[j]] > 0: 
            my_dict[d[j]] = my_dict[d[j]]-1 
        else:  
            find = False
            print("Nooooooo")
            break 

        
    if find == True: 
        print("yayyyyyy")
