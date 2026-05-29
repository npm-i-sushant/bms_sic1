import numpy as np 

array_1 = np.full((2,2),1)
array_2 = np.full((2,2),2,dtype='float')

print(type(array_1))
print(type(array_2[0][0]))