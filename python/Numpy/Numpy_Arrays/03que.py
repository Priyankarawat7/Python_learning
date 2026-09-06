import numpy as np

matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

# matrix me se sirf woh elements nikalo jo 40 se greater hain.

bool_arr=matrix>40

print(matrix[bool_arr])

# matrix me se saare elements nikalo jo 100 se greater hain.

bool_matrix=matrix>100

print(matrix[bool_matrix])