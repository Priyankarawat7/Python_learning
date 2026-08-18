# user-Defined
# Function are a block of reuseable code you can execute multiple times
# def hello():
#     print('hii priyanka')

# hello()


# # def sum(a,b):

# #     print(f"The sum of your num is:- {a+b}")
                
# # sum(12,34)


# #Three type of arguments

# #!. Positional arguments

# def greet(name,age):
#     print(f"your name is {name} and your age is {age}")

# greet('priyanka',22)

# #Keyword arguments
# greet(age=22,name="bhumi")



# ##default arguements space
# def sum(a=21,b=52):

#     print(f"The sum of your num is:- {a+b}")
                
# sum()



# #To check if the string is pallindrome or not


# def pallindrome(st):

#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev+=st[i]

#     if rev==st:
#         print(f" {st} is a pallindrome")
#     else:
#         print(f"{st} is Not a pallindrome")

# pallindrome("naman")


def wish():
    return 'Thanks for your exprience' #return return back krta if we call only wish(         )

print(wish())
                   