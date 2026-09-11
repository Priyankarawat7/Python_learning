#to DAta Frames
#when you combine multiple series is called dataFrames

#Creating dataFrame

import pandas as pd
import numpy as np

data = {
    "Name": ["Priya", "Riya", "Aman", "Karan", "Neha", "Rahul", "Simran", "Arjun"],
    "Age": [20, 21, 22, 20, 23, 21, 22, 20],
    "City": ["Chandigarh", "Mohali", "Delhi", "Chandigarh", "Delhi", "Mohali", "Chandigarh", "Delhi"],
    "Course": ["BCA", "BCA", "BTech", "MCA", "BCA", "BTech", "MCA", "BCA"]
}

df=pd.DataFrame(data)
#print(df)

# Data List
data_list = [
    ["Priya", 20, "Chandigarh", "BCA", 85],
    ["Riya", 21, "Mohali", "BCA", 72],
    ["Aman", 22, "Delhi", "BTech", 91],
    ["Arjun", 20, "Delhi", "BCA", 64]
]

columns=["Name","Age","City","Course","marks"]
df2=pd.DataFrame(data_list,columns=columns)
#print(df2)



#Selection and indexing of column
# print(df2['Name'])
# print(df2[['Name','City']])


#Creating a new column
df2['Attendance']=[80,60,60,30]
#print(df2)

#Removing Column
#INplace->remove permanently 
#print(df2.drop('Attendance',axis=1))
# df2.drop('Attendance',axis=1,inplace=True)
# print(df2)
#Selecting row

# print(df2.loc[[0,1]])
# print(df2.loc[0:])
                
#Selecting subset of rows and column
# selecting particular portion
#print(df.loc[[0,1]][["City","Course"]])

#print(df.loc[[0,1]][["Name","Age"]])

#Condtional Selection

#if only want to see those people whose age is >20
#print(df2[(df2["Age"]>20) & (df2["City"]=='Delhi' )])


print(df2[df2["Age"]>20])

print(df)

                                        

