# proram to find number of lines in a given file and content of file
# author: Deepak kumar jha 
src=input("Enter file Name : ")
try:
    fhandle=open(src,'r')
except:
    print("No such File Name Exist")
    quit()
cnt=0
for line in fhandle:
    cnt=cnt+1
print("Numner of lines in file",src.capitalize(),"is = ",cnt)

src2=input("Enter file Name : ")
try:
    fhandle2=open(src2)
except:
    print("No such File Name Exist")
    quit()

print("printing content of file ")
inp=fhandle2.read()
print(src2,"has length = ",len(inp))

print("Reading first 200 char from ",src2)
print(inp[:200])

for line in inp:
    if line.startswith('print'):
        print(line)
