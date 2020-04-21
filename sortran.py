n =input() 
n=int(n)
# input the array 
arr = [int(x) for x in input().split("\n")]
arr.sort()
for i in range(n):
    print(arr[i],end=" ")
