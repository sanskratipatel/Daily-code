a = [1,2,3,4,5] 

b = map(lambda x:x +2 , a) 
print(list(b)) 

def plus_two (x) :
    return x+2 

c = map(plus_two,a) 
print(list(c)) 
d = [x*2 for x in a] 
print(d)