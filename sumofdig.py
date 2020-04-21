n=input("enter a number containing more than one digit\n")
x=len(n)
i=0
sum=0
while i<x:
    sum+=int(n[i])
    i+=1
print(f"sum of digit of {int(n)} is = ",sum)