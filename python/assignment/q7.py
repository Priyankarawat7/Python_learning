# Prime or Composite number

n=int(input("Enter a number: "))

sum=0
count=0

for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if count==2:
    print("Prime no")
else:
    print("Composite Number")