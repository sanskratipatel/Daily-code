str1 = "anagraam" 
str2 = "nagaram" 


if len(str1) != len(str2): 
    print("Not equal")  
else:
    s1 = sorted(str1) 
    s2 = sorted(str2)  
    print(s1 , s2)
    if s1 == s2 :
        print("Equal") 
    else:
        print("Not Equal") 
my_dict = {}

for i in range(0 , len(str1)) :
    if str1[i] not in my_dict:
        my_dict[str1[i]] = 1 
    else: 
        my_dict[str1[i]]=my_dict[str1[i]]+1 

for j in range(0 , len(str2)) : 
    if str2[i] not in my_dict :  
        print("Nooooooooo")
        break 
    else : 
        if  my_dict[str2[i]]  == 0 :  
            print("Nooooo")
            break
        my_dict[str2[i]] =  my_dict[str2[i]] -1 
        

