n=input("enter a string\n")
i=0
temp=""   # creating var for storing and checking if codn

for i in range(len(n)):
    if n[i] not in temp:
        temp+=n[i]
        print(f"{n[i]} : {n.count(n[i])} ")   # here we are printing different alphabet
