point2_d = [(1,2),(15,1) ,(5,-1),(10,4)] 

sort = sorted(point2_d,key = lambda x :x[1])  
print(sort)  
s = sorted(point2_d, key=lambda x : x[0] + x[1])  
print(s)


my_dict = { 1:"Oranges",2 : "Apples" , 3 :"Banana"}

values = list(my_dict.values()) 
values.sort()
new_dict = {}
for i in range(0 ,len(values)) : 
    for key in my_dict : 
        if my_dict[key] == values[i] : 
            new_dict[key] =values[i]
print(new_dict) 


new_dict1 = dict(sorted(my_dict.items() ,key =lambda x: x[1])) 
print(new_dict1)