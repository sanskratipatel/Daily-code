s = "cccaaa" 
# s = "tree" 

my_dict = {} 

for i in range(0 , len(s)) :
    if s[i] not in my_dict :
        my_dict[s[i]] = 1 
    else:
        my_dict[s[i]] = my_dict[s[i]] +1  
result = ""
# sorted_char = sorted(my_dict.items() , key=lambda x :x[1],reverse=True) 
sorted_char = sorted(my_dict.items() , key=lambda x :(-x[1],x[0])) 
for ch ,freq in sorted_char :
    result = result + (ch * freq) 

print(result)