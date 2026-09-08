import numpy as np


data=np.array([
    [18,85,78],
    [19,92,88],
    [18,35,70],
    [20,90,85]
])

# get the shape of the matrix
#print(data.shape)

# # find the average age of students
#print(np.mean(data[:,0])) #all rows column 0

# #Extract math marks of all students

# print(data[:,1].sum())

#find the highest science mark

#print(np.max(data[:,2]))

#get details of the student who scored more  than 90 in Math

#print(data[data[:,1]>90])


#Increase Math of all students by 5

#print(data[:,1]+5)

# find how many students are younger than 19


print(len(data[data[:,0]<19]))


#Calculate the average marks in each subject (column-wise mean)
 
print(np.mean(data[:,1:],axis=0))

#Get data of students who scored atleast 80 in both subjects

print(data[(data[:,1] >=80) & (data[:,2]>=80)])

#Replace all Science marks <75 with 0

data[data[:, 2] < 75 ,2]= 0


print(data)