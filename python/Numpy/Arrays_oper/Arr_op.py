import numpy as np

# Arithmetic operations

#size must be same of arrays while performing some operations

a1=np.array([1,2,3,4,5])
a2=np.array([6,7,8,9,10])

# print(a1+a2)
# print(a1-a2)
# print(a1*a2)
# print(a1/a2)
# print(a1//a2)
# print(a1**a2)

# BroadCasting->it means you are performing some operations 
l=[10,20,30,40]
arr=np.array(l)

#print(arr+10)

a=np.arange(1,21).reshape(5,4)

#print(a*10)

# Deep and Shallow copyright

# When you are performing some operation in array 
# it will create there own space and doesn't affect original arrays is known as shallow copys
b=np.arange(1,21)
slice=b[:5]

c=slice*10
# print(c)
# print(b)

   
# Deep copy will affect in the orignal arrays

#if you are copying entire array in the variable and 
#then you doing some changes it will also affect in the original array

c=b
c[0]=55
# print(c)
# print(b)

# matrix operations

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

C=np.dot(A,B)
# print(A@B)
# print(B)
# print(C)

Trans=A.T

#print(Trans)

# advance arrays manipulation

#To Join two arrays
#you can't stack two matrix
# stacking Arrays

p=np.array([1,2,3,4])
q=np.array([5,6,7,8])

# print(np.vstack((p,q)))
# print(np.hstack((p,q)))

# print(np.column_stack((p,q)))

# spliting arrays

d=np.arange(16).reshape(4,4)

#print(d)

#print(np.hsplit(d,4))

print(np.vsplit(d,4))