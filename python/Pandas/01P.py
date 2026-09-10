import pandas as pd
import numpy as np
labels=['a','b','c']
list=[10,20,30]
arr=np.array([30,40,50])
d={'p':10,'q':20,'r':30}

# print(labels)
# print(list)
# print(my_array)
# print(d)

#print(pd.Series(list))

#you can set out customize labels
#print(pd.Series(list,index=labels))

#you create series withh arrays

print(pd.Series(arr))

#you create also dicternary

print(pd.Series(d))
