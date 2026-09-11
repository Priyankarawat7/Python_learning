import numpy as np
import pandas as pd

# Missing data

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 21, np.nan, 22, 20],
    "Marks": [85, np.nan, 72, 90, np.nan],
    "City": ["Delhi", "Chandigarh", np.nan, "Mohali", "Delhi"],
    "Attendance": [90, 85, 78, np.nan, 95]
}

df=pd.DataFrame(data)


#print(df)


# finding missing Data

# print(df.isna().sum())

# print(df.isna().any())


# Removing Missing Data
# removing the value in the basis of rows
#print(df.dropna())
#print(df.dropna(thresh=4))

#Filling the missing Data
#COlumn wise selection to fill
#print(df.fillna(0))

# values={'Name':'100','Age':20,"City":'goa',"Attendance":40}
# fill_values=df.fillna(value=values)
# print(fill_values)

print(df.fillna(df.mean(numeric_only=True)))
