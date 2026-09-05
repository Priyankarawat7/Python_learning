"""

we use curly braces in dictonary
it includes key and value pairs


Mutables:-you can add values but not keys

Duplicates- key can be unique but values can be common

Order= follow insertion order

Hetrogenous- keys and values like integers ,list or even anothrt dictinary


you can  update the values but not the key
"""

# d={1:"h",2:"priya"}

# d[2]="rawat" #Updating when value is exist

# d[10]="nia" #Creating 

# del d[2] #delete
                      
# d.update({3:"bhumi"})

# print(d)


"""
Dictonary in Traversing

"""

a={10:100,20:200,30:300,40:400}

#for i in a.values():  #if you write a.value you can directly access value
  # print(i)


"""

Dictornary methods



Deep
It means jab ap ksi ek variable ki copy dusre variable mai krte ho 
and the if you update few values it can also update in first one variables 


 and Shallow Copy ->for shallow copy we can use .copy() and 
 if you update in 2nd variable it can't update in the first variable
"""

# Deep Copy
p=[1,2,3,4,5]

# b=p

# b[0]=100

# print(p)

#shallow copy

# b=p.copy()

# print(p)


o={10:100,20:200,30:300}
print(o.items())


