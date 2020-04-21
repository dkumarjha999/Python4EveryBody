n1,n2=input().split(",")
n1=int(n1)
n2=int(n2)

t=1
for i in range(n1):
    for j in range(n2):
        print(t,end='')
        t=t+1
    print()