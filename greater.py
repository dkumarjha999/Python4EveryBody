def greater(a,b):
    if(a>b):
        return a
    else:
        return b    
x,y=input("enter two number sep by , ").split(",")
x=int(x)
y=int(y)
print(f"greter of {x} , {y} is = ",greater(x,y))
