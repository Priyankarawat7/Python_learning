
# number= int(input("Enter the Integer:-"))

# for i in range(number):
#     print("Hello world")


#print n natural no.

#n=int(input("Enter the number:-"))

# for i in range(1,n+1):
#     print(i)


#Reverse
# for i in range(n, 0,-1):
#     print(i)


#Print the table

# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")

#Sum up to n terms
                                
#sum=0
# for i in range(1,n+1):

#     sum+=i
#     print(sum)

#Fact of a num
# fact=1

# for i in range(1,n+1):
#     fact*=i
#     print(fact)

#print the sum of all odd & even no. seperately

# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
        
#     else:
#         odd+=i
       

# print(f"your even and odd sum are {even},{odd}")

#print all the factors

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

#perfect no.

# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i

# if sum==n:
#     print("Your number is perfect")

# else:
#     print("Your number is not perfect")       

# print(sum)


#Check wheather the number is prime or not

# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
#        # print("Factors",count)

# if count==2:
#     print("It's a Prime no")
# else:
#     print("Not a prime number")


#Print the Reverse 
# a= "SHERYIANS"
# b=""
# print(a[::-1]) #Reverse order

# for i in range(len(a)-1,-1,-1):
#     b+=a[i]

# print(b)

#Check the string is pallindrome or not

# a= input("Enter a string:-")
# b=""
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]

# if b==a:
#     print("Pallinerome")

# else:
#     print("Not pallinedrome")

a="sdg1ytr%^&*&^%$"
char=0
dig=0
spchr=0

for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchr+=1

print( f"your Digits are {dig}\n your aplhabets are {spchr}\n and your characters are {char}")

           














