# Merging  joining and concatination
import numpy as np
import pandas as pd
#merging 2 dataframes

employees = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104, 105],
     "Employee_Name": ["Rahul", "Priya", "Aman", "Neha", "Rohit"],
    "Department": ["IT", "HR", "Finance", "IT", "HR"]
})

salaries = pd.DataFrame({
   "Emp_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
"Salary": [35000, 42000, 38000, 45000, 50000, 36000, 47000, 52000, 40000, 55000],
"Bonus": [3000, 5000, 4000, 6000, 7000, 3500, 5500, 8000, 4500, 9000]
})

# print(employees)
# print(salaries)

#print(pd.merge(employees, salaries, on="Emp_ID"))
# print(pd.merge(employees, salaries, on="Emp_ID",how='inner'))


# print(pd.merge(employees, salaries, on="Emp_ID",how='outer'))
# print(pd.merge(employees, salaries, on="Emp_ID",how='left'))
# print(pd.merge(employees, salaries, on="Emp_ID",how='right'))

#Concatination of 2 dataFrames

products = pd.DataFrame({
    "Product_ID": [201, 202, 203],
    "Product_Name": ["Laptop", "Mouse", "Keyboard"],
    "Price": [55000, 1200, 2500]
})

#print(products)
students = pd.DataFrame({
    "Student_ID": [201, 202, 203],
    "Name": ["Anjali", "Karan", "Simran"],
    "Marks": [85, 92, 78]
})

#print(students)


# print(pd.concat([products,students]))

# print(pd.concat([products,students],axis=1))

# print(pd.concat([products,students],axis=0))


#joining of 2 dataframes

orders = pd.DataFrame({
    "Order_ID": [301, 302, 303],
    "Customer": ["Riya", "Aman", "Neha"],
    "Amount": [1200, 2500, 1800]
})

#print(orders)

employees2 = pd.DataFrame({
    "Emp_ID": [401, 402, 403],
    "Name": ["Rohit", "Simran", "Karan"],
    "Salary": [30000, 45000, 38000]
})

#print(employees2)

#print(orders.join(employees2))

print(orders.join(employees2,how='outer'))
print(orders.join(employees2,how='inner'))

