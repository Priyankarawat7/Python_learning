import numpy as np


# Create a 3×3 random integer matrix containing values between 1 and 100.
#a=np.array([[]])

rand=np.random.randint(1,101,size=(3,3))

#print(rand)

# For this array:

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

# find its ndim, shape, size, and dtype.

# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)


# Create an array and find its maximum, minimum, sum, and mean.
c=np.array([5,10,15,20,25,30])

# print(c.max())
# print(c.min())
# print(c.sum())
# print(c.mean())

# Sort this array:
p = np.array([50, 10, 40, 20, 30])
p.sort()

print(p)

# Find the index of 30 in:
d = np.array([10, 20, 30, 40, 50])

print(np.where(d==30))


# Create an array [1, 2, 3, 4, 5] and calculate the square of every element.

sq=np.array([1, 2, 3, 4, 5])

#print(sq*sq)
# Create an array containing 1 to 12 and reshape it into a 3×4 array.

s=np.arange(1 ,13)

print(s.reshape(3,4))