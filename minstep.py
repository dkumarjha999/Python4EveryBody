arr = [int(x) for x in input().split()]
arr1 = sorted(arr)
count = 0
for i in range(len(arr)):
    if arr[i] == arr1[count]:
        count+=1
print(len(arr)-count)