nm,ch=input("enter name , character\n").split(",")
print("length = ",len(nm))
nm=nm.strip()
ch=ch.strip()  #if we want we can use nm.lower()here also
nm=nm.lower()
ch=ch.lower()
cn=nm.count(ch)
print(f"character {ch} repeated ",cn," times")