# l=[-45,20,12,34-87,-34]

# for i in l:
#     if(i>=0):
#         print('postive:',i)

# print("Negtive elements arre")   

# for i in l:
#     if(i<0):
#         print(i)



#Mean
l=[12,23,45,6,7,86,98,87]

# sum=0
# for i in l:
#     sum+=i


# print(sum/len(l))

#Greatest elements in index to

# largest=0
# index=0

# for i in range(len(l)):
#     if(l[i]>largest):
#          largest=l[i]
#          index=i

#print("your largest number",largest,"and index",index)

#2nd largest

# largest=l[0]
# sec_larggest=l[0]

# for i in l:
#     if(i>largest):
#         sec_larggest=largest
#         largest=i
#     elif i>sec_larggest:
#         sec_larggest=i
      

# print("Second largest",sec_larggest)

#check if list sorted or not


sort=0
first_el=0
sec_el=0

for i in range(len(l)-1): 
    if(l[i]<l[i+1]):
        continue
    else:
       print("your list is not sorted")
       break
else:
    print("your list is sorted")












#





 