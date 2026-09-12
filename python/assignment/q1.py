
#1. Largest and Smallest of Three Numbers
a=input("Enter first number:-")
b=input("Enter second number:-")
c=input("Enter third number:-")


if a >= b and a >= c:
    print(a,"is largest")
elif b >= a and b >= c:
    print(b," is largest")
else:
    print(c,"is largest")

# Smallest
if a <= b and a <= c:
    print(a," is smallest")
elif b <= a and b <= c:
    print(b,"is smallest")
else:
    print(c," is smallest")



# print("Largest no. is",max(a,b,c))

# print("Smallest no is", min(a,b,c))

