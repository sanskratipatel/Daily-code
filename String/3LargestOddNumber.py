num = "6128246" 
# num = "546827" 
str1=num 
find = False
for i in range(len(num)-1 , -1 , -1) :  
    if int(num[i]) % 2 != 0 :
        find = True 
        print(str1) 
        break 
    str1 = str1[:-1] 

if find == False: 
    print("Zero Odd number")
