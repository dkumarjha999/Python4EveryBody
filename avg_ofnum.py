# author: Deepak kumar jha 

# program to find avg. of numbers
cnt=0
sum=0.0
while True:
    inp=input("Enter a value : ")
    if inp=='done':
        break
    try:
        val=float(inp)
    except:
        print("Bad Data")
        continue
    sum=sum+val
    cnt=cnt+1
print("sum = ",sum,",count = ",cnt,",average = ",sum/cnt)
