a = [2,3,4,5,6,7,7,6] 

p = filter(lambda x : x%2==0 , a) 
print(list(p)) 

def even (x) :
    return (x%2==0) 

d = filter(even,a) 
print(list(d))
r = [x for x in a if x%2==0 ] 
print(r)