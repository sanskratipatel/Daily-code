str1 = "{}" 

stack = [] 
invalid = True
for i in range(0 , len(str1)) :
    if str1[i] == '{' or str1[i] == '(' or str1[i] == '[':
        stack.append(str1[i]) 
    else : 
        if len(stack) ==0 :
            print("Invalid Parenthis1")  
            invalid = False
            break 

        e = stack.pop() 
        if e == '(' and str1[i] != ')' or e == '{' and str1[i] != '}' or e == '[' and str1[i] != ']' :
            print("Invaalid Parentthis  0" ) 
            invalid = False
            break 
if invalid == True: 
    if len(stack) != 0 : 
        invalid = False 
        print("Invalid Parenthis") 

if invalid == True :
    print("Correct parenhthis")

