import random as r
computer=r.randint(1,10)

guess=3
while guess>0:
    user=int(input("enter a number"))
    if user==computer:
        
        print("the user got a point")
    else:
        guess-=1
        print("try again")
        print("the chances are:",guess)
        
if guess==0:
    print("Computer Win")