import numpy as np 


zeroes = np.zeros((3,4)) 
print("Zeroes Array = ",zeroes)


ones = np.ones((2,3)) 
print("onss = ",ones) 

full_num = np.full((2,4) ,8) 
print("full num = ", full_num) 


random_method =np.random.random((2,3)) 
print("random value = \n  ", random_method) 

sequence = np.arange(0,11,2) 
print("sequence = ",sequence) 


# Zeroes Array =  [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
# onss =  [[1. 1. 1.]
#  [1. 1. 1.]]
# full num =  [[8 8 8 8]
#  [8 8 8 8]]
# random value = 
#    [[0.858033   0.91209083 0.12002158]
#  [0.29935135 0.12991524 0.40433828]]
# sequence =  [ 0  2  4  6  8 10]