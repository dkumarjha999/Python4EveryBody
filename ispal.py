def ispal(s):
    t=s
    m=s[::-1]
    if t==m:
        return True
    return False

x=input("enter a string ")
print(ispal(x))