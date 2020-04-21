'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list
of words using the split() method. The program should build a list of words. For each word on
each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt

'''


fname = input("Enter file name: ")
try:
    fh = open(fname,'r')
except:
    print("Invalid file name ")
    quit()

lines=list()
sublist = list()
for line in fh:
    line=line.rstrip()
    lines.append(line)

for x in lines:
    val=x.split()
    sublist=sublist+val

sublist.sort()
# list(dict.fromkeys(sublist))   # function list(dict.formkeys(listname))  to remove duplicate value from list

res = list()      # removing duplicate from list
for i in sublist:
    if i not in res:
        res.append(i)

print(res)


