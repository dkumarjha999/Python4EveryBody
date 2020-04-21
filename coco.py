nm,age=input("enter your name, age separated by comma\n ").split(",")
nm=nm.strip().lower()
age=int(age)
if(nm[0]=='a'and age>=10):
    print("you can watch movie\n")
else:
    print("you can't watch movie\n")