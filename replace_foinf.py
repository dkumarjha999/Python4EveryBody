x=input("enter a string \n")
print(x.replace(" ","_"))
c=input("enter substring you want to find \n")
c=c.strip()   #to remove space 
print(f"sub string {c} found at ",x.find(c,5))
