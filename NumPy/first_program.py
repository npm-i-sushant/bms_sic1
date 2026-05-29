import numpy as np

arr_1 = np.zeros(3)
arr_2 = np.zeros((1,4))
arr_3 = np.zeros((3,3))

try:
    print(arr_1)
    print(arr_2)
    print(arr_3)
except:
    print("Enter correct input")
