
import random

num=random.randint(1,11) #to generate random number

# print(num)
tries=0

while True:
    guess=int(input("Please guess your number:- "))

    tries+=1

    if num==guess:   
        print(f"You are right! {tries}")
        print("Total tries:", tries)
        break
    elif num<guess:
        print("go a  little lower")
    elif num>guess:
        print("go a little higher")
    else:
        print("Sorry, you are wrong")


