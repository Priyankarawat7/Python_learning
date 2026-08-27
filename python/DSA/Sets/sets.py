"""
Mutable->you can change the value
Duplicates->cannot have any duplicate value (only unique)
unordered->sets are unorderd you cannot access them through index values

hetrogenous->semi-hetrogenous store some data types like strings,numbers,tuples,not everything

"""

#how to create a set

#s={} #it is a dictonary

s={1,2,3,4,4,5,5} # you can change the value

print(s) #{1, 2, 3, 4, 5}


#print(s[2]) # 'set' object is not subscriptable you can't access



"""
How sets stored value in python
"""

#Ordered ordered is provided                   
b=hash("hello")

print(b)

c=hash((1,2,3,444))

print(c)


"""
Set Traversing
cannot be traversed using the inde values cause 
it is unordered and has no index
"""

p={2,3,4,6,5}

#for i in p:
   # print(i) #random value will be given

"""
Set method
"""

# p.add(8), p.remove(),p.discard(),p.clear(),p.pop()
# print(p)

o={23,4,45,6,56}
n={2,3,4,5,5}

union_set=o.union(n)
intersection_set=o.intersection(n)
difference_set=o.difference(n)
symmetric_sets=o.symmetric_difference(n)


print(union_set)
print(intersection_set)
print(difference_set)
print(symmetric_sets)





