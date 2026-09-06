import numpy as np

# Numpy indexing and slicing of vectors

arr=np.arange(11,21)
# print(arr)

 
# # Indexing 
# print(arr[6])

# # Slicing- yo are removing a portion
# #Start,end,step
# print(arr[1:5])
# # there are some default value as well

# print(arr[:5])
# print(arr[:])

# print(arr[3:])

# print(arr[3::2])



# Numpy indexing and slicing of matrix

a=np.arange(1,31).reshape(6,5)

#Indexing are happen in rows and column in matrix
#print(a[0])


#print(a[5,4])


# Slicing
#print(a[0:2,1:3])

# print(a[3:,3:])

# print(a[:,2])

# boolean Indexing


b=np.arange(11,21)

bool_index=b%2==0

b=b[bool_index]
print(b)


