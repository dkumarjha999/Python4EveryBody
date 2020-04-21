def add(num1,num2):
    return num1+num2

a,b=input("enter two number sep by ,").split(",")
a=int(a)
b=int(b)
total=add(a,b)
print(f" total of {a} , {b} is = ",total)

# smae fun for atring concatination
fir_nm=input("enter first name")
sec_nm=input("enter second name")
th=add(fir_nm,sec_nm)
print(f" new string using {fir_nm} , {sec_nm} is = ",th)

