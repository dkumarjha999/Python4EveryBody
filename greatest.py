def greatest(a,b,c):
    if a>b and a>c:
        return a;
    elif b>a and b>c:
        return b
    else:
        return c
x,y,z=input(" enter three number sep by ,").split(",")
x=int(x)
y=int(y)
z=int(z)
print(f"greatest of {x} ,{y}, {z} is = ",greatest(x,y,z))


# kiss keep it simple stupid