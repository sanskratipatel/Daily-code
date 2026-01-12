from collections import Counter 

a = "aaabbbcccdd" 
my_counter = Counter(a) 
print(my_counter) 

print(my_counter.items()) 
print(my_counter.most_common())  
print(list(my_counter.elements())) 
