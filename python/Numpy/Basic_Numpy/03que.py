import numpy as np


# Create an array containing 1 to 12 and reshape it into a 2×6 array.
arr=np.arange(1,13)

#print(arr.reshape(2,6))

# Create an array containing 1 to 12 and reshape it into a 2×2×3 array.

#print(arr.reshape(2,2,3))

# Try to reshape an array of 10 elements into 3×4. What happens and why?

a=np.arange(1,11)

#print(a.reshape(3,4))  #cannot reshape array of size 10 into shape (3,4)
# Reason:
# 3 × 4 = 12 elements required, but array mein only 10 elements hain.

# Create an array [1, 2, 3, 4] and resize it to 2×3 using resize().

b=np.array([1,2,3,4])
#b.resize(2,3)
#print(b)

# cannot resize an array that may be referenced by another object.
# It is possible that this is a false positive.
# If you are sure that the array is uniquely referenced, set refcheck=False.


# Take an array of 1 to 12, reshape it to 3×4, and then reshape it again to 2×6.
c=np.arange(1,13)

# print(c.reshape(3,4))
# print(c.reshape(2,6))
# 🔥 Mini Challenge: 
# Create numbers from 1 to 25, convert them into a 5×5 matrix, then find its shape, ndim, size, max, min, sum, and mean.

d=np.arange(1,26)

p=d.reshape(5,5)
print(p)
print(p.shape)

print(p.ndim)

print(p.size)

print(p.max())
print(p.min())
print(p.sum())

print(p.mean())

