d1={10:100,20:200,30:300}

d2={40:400,50:500,60:600}

# for i in d2:

#     d1[i]=d2[i]
   

# print(d1)


#Print the sum
sum =0

for i in d1:
    sum=sum+d1[i]

#print(sum)


#Count the freq. of each element in a list

a=[1,1,1,2,3,3,4,5,6,6,2,4,4,3]
count=0
d={}
#dict={1:3,2:2,3:3,4:4,5:1,6:2}
for i in a:
    if i in d.keys():

        d[i]+=1
    else:
        d[i]=1


print(d)


#Combined two dictonary    
# 
for i in d2:
    if i in d1.keys():

        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]

print(d1)     
        



