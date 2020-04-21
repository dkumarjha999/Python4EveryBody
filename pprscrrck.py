n=input("enter number of times you want to play")
n=int(n)
x=0
y=0
dr=0
for i in range(n):
    a,b=input("enter two num sep by ,").split(",")
    a=int(a)
    b=int(b)
    if a>b:
        x+=1
    elif b>a:
        y+=1
    else:
        dr+=1
print(f"you played {n} times in which first won {x} times and second won {y} times draw {dr} times ")
if x>y:
    print(" finally first won")
elif y>x:
    print("finally second won")
else:
    print(" finally match draw")
    
        
    