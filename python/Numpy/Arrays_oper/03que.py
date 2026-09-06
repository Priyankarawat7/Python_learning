import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [10, 20],
    [30, 40]
])

#result=np.vstack((a,b))


#print(result+5)


p = np.array([1, 2, 3])
q = np.array([10, 20, 30])

result=np.hstack((p,q))

bool_arr=result>20
print(result[bool_arr])


