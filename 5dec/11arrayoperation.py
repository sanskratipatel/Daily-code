import numpy as np 

a1 =np.arange(1,13).reshape(3,4) 
a2 = np.arange(12,24).reshape(3,4) 
# Arthematical Operation
print(a1) 
print()
print(a1 + 2) 
print()
print(a1 - 2) 
print()
print(a1 * 5) 
print()
print(a1 // 2) 
print()
print(a1 % 2) 
print()
print(a1 ** 2) 
print()


# relational Operation 
print(a2)  
print()
print(a2 > 2) 
print()
print(a2 >100)
print()
print(a2 ==12)
print() 

# VECTOR Operation  

print(a1 + a2)
print() 
print(a1 - a2)
print()
print(a1 * a2)
print()
print(a2 // a1)
print()