str1 = "(1+(2+3)+(((8)/4)))+1" 
stack = [] 
curr_depth = 0 
max_depth = 0
for i in range(0 , len(str1)):
    if str1[i] in "({[":
        stack.append(str1[i]) 
        curr_depth = curr_depth+1 
        max_depth = max(max_depth,curr_depth) 
    elif  str1[i] in "}])": 
        curr_depth =curr_depth-1 
        stack.pop() 

print(max_depth)
         
    
