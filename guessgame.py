a=23
n=input("enter a two digit number as guess\n")
n=int(n)
if(n==a):
    print(" your guess is absolutely right \n you won \n")
else:
    if(n>a):
        print("too high\n")
    else:
        print("too low\n")