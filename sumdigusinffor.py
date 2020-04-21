n=input("enter a number\n")
sum=0
for i in range(len(n)):
    sum+=int(n[i])
print(f" sum of digit of number {int(n)} is = ",sum)