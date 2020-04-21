age=input("please enter your age\n")
n=int(age)
if n<=0:
    print("you can't watch\n")
elif 0<n<=3:
    print("ticket price : Free\n")
elif 4<=n<=10:
    print("ticket price : 150\n")
elif 11<=n<=60:
    print("ticket price : 250\n")
else:
    print("ticket price : 200\n")