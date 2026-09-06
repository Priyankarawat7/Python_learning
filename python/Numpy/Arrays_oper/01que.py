import numpy as np


#Spliting Arrays
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])


#print(np.split(arr,4))

# 2. Splitting Matrix

# Matrix:

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])


#print(np.vsplit(matrix,2))



print(np.vstack((a,b)))


print(np.hstack((a,b)))






