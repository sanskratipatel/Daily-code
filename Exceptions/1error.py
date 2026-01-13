try:
    a = 5 /0 
except :
    print("An error Accured") 

try:
    a = 5 /1 
    b = [1,2,3]   
    
    c = 5 + 9 
    print(c)
    print(b[10])
except ZeroDivisionError :
    print("Errorr") 
except IndexError :
    print("error")
except Exception as e:
    print("An error Accured",str(e)) 

else:
    c = 45 + c 
    print(c) 
finally : 
 print("Finaaly")