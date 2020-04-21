
a=input().split(" ")
n=int(len(a)) 
# arr = [4, 3, 2, 1] 
c=0
while(True):
    for i in range(n-1):
        x=0
        if(int(a[i+1])<int(a[i])):
            t=a[i]
            a[i]=a[i+1]
            a[i+1]=t
            x+=1
        if(x>0):
            c+=1
            if(x<1):
                break
    if(c<1):
        break            
print("total moves = ",c)

