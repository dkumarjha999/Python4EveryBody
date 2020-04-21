def fib(n):
    if n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
x=input("enter a limit ")
x=int(x)
for i in range(1,x+1):
    print(fib(i),end=" ")