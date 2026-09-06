import numpy as np

matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

# Matrix Indexing & Slicing
# Matrix ki 2nd row nikalo.

#print(matrix[1])
# Matrix ka 3rd column nikalo.
print(matrix[:,2])
# Matrix ke top-left 2×2 elements nikalo.

#print(matrix[0:2,0:2])
# Matrix ke last 2 rows aur last 2 columns nikalo.

print(matrix[2:,2:])