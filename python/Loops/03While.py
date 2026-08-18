"""
While Loop

useful when the number of iteration is unknown

while condition:
    //statement

"""

# a=1

# while  a<=30:
   
#     print(a)
#     a+=1


a=int(input("Enter the digit:-"))

# while a>0:
#     print(a%10)
#     a=a//10


#Reverse
# rev=0
# while a>0:
#     rev=rev*10+ a%10
#     a=a//10

# print(rev)   


#Pallinedrome
rev=0
copy=a
while a>0:
    rev=rev*10+ a%10
    a=a//10

if copy==rev:
    print("Pallinedrome")
else:
    print("Not pallindrome") 




              