from itertools import groupby 

def smaller_than_three(x) :
    return x<3
a = [1,2,3,4,5,6] 
group_obj = groupby(a,key=smaller_than_three) 
for key ,val in group_obj:
    print(key,list(val))
