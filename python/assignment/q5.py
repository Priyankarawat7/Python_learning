#Series: 1 + x + x² + ... + x

x= int(input('Enter x:'))
n=int(input("Enter n:"))

sum=0;

for i in range(n+1):
    sum=sum+x**i

print("Sum",sum)

# Series: 1 - x + x² - x³ + ... ± xn

# for i in range(n+1):
#     if(i%2==0):
#       sum=sum+x**i
#     else:
#       sum=sum-x**i

# print("sum =",sum)

#Series: x + x²/2 + x³/3 + ... + x■/n

# for i in range(1,n+1):
#    sum=sum+(x ** i)/i

# print("Sum:",sum)

#Series: x + x²/2! + x³/3! + ... + x■/n!

fact=1
for i in range(1,n+1):
   fact=fact*i
   sum=sum+(x**i)/fact

print('Sum :',sum)
   

