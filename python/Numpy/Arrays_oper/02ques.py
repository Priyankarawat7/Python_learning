import numpy as np

#Deep vs Shallow Copy

arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy() 
view_arr = arr.view()

arr[0] = 100

# print(copy_arr)#[10,20,30,40]
# print(view_arr) #[100,20,30,40]



#BroadCasting

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

x = np.array([1, 2, 3])


print(arr+x)



a = np.array([
    [10, 20],
    [30, 40]
])

#print(a*5)


#Arithmetic Operations


a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 10])


print(a+b)
print(a-b)
print(a*b)
print(a/b)