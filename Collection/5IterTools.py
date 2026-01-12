from itertools import combinations ,combinations_with_replacement,accumulate
a = [1,2,3,4] 
import operator
comb = combinations(a,2) 
print(list(comb)) 

comb_wr = combinations_with_replacement(a,2) 
print(list(comb_wr))
b = [1,2,5,3,4] 
acc=accumulate(a) 
print(list(acc)) 
ac1 = accumulate(b,func=max) 
print(list(ac1) )
ac2 = accumulate(a,func=operator.mul) 
print(list(ac2))