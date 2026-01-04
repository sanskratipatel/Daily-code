n= 1211 
n1 = n

rev = 0 
count = 0 

while(n>0) : 
    rev = rev *10 + (n %10) 
    n = n//10 
    count =count +1 
print("Reverse = ",rev) 

if rev == n1 : 
    print("Pallindrom") 
else: 
    print("No Pallindrom")