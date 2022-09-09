from random import randint
def random_number():
    reply1 = input("Type in woof or meow:")
    if reply1 == "woof":
        print("Here is a random  number:"+str(randint(1,100)))
    elif reply1 == "meow":
        print("Here is a random  number but from 1-50:"+str(randint(1,5)))
    else:
        print("Not what I asked, try again")
random_number()
