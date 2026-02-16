str1 = "MDAM"
rev = str1 
ans = ""
for i in range( len(str1)-1,-1,-1 ): 
    ans = ans + str1[i] 

if ans == rev:
    print("True") 
else:
    print("False")

