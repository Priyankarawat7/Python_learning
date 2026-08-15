#Ques-1
# first_num= int(input("Enter 1st number: "))
# second_num= int(input("Enter 2nd Number: "))

# if(first_num>second_num):
#     print(first_num," it is greater")
# elif second_num>first_num:
#     print(second_num,"is greater")
# else:
#     print("Both are equal")



#Ques-2
# gender= (input("Choose the gender:-"))

# if(gender=="female"):
#     print("Good Morning Mam")

# elif(gender=="male"):
#     print("Good Morning Sir")

# else:
#     print("Unknown Gender")

#Ques-3

# Num=int(input("Enter the Number :"))

# if(Num%2==0):
#     print("Number is Even")

# else:
#     print("Number is Odd")


#ques-4
# Name= str(input("Enter name: "))
# age=int(input("Enter age: "))

# if(age>=18):
#     print("Hello",Name,"you are a valid voter")
# else:
#     print("Hello",Name,"you are not a valid voter")

#ques-5

# year=int(input("Enter year:-"))

# if(year%100==0 and year%400==0):

#     print("The year is a leap year")
# elif(year%100!=0 and year %4 ==0):
#     print("The year is a leap year")
# else:
#     print(" Normal year")

#Ques-6

t=int(input("Enter temprature:-"))

if t<0:
    print("Freezing Cold")

elif t>=0 and t <10:
    print("Very COld ❄️")
elif t>=10 and t<20:
    print("Cold ⛄")
elif t>=20 and t<30:
    print("Pleasent ☁️")
elif t>=30 and t<40:
    print("Hot 🔥")
else:
    print("Very Hot 🌇")