s = "tree" 
my_dict = {} 
result = ""
for i in range(0 , len(s)) :
    if s[i] not in my_dict :
        my_dict[s[i]] = 1 
    else:
        my_dict[s[i]] = my_dict[s[i]] +1 

sorted_char = sorted(my_dict.items(), key = lambda x:x[1] , reverse=True)  
print(dict(sorted_char))



for ch , freq in sorted_char : 
    result = result + (ch * freq)  

print(result)