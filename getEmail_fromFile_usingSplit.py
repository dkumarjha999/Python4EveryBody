#author deepak kumar jha
'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with
'From ' like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the
entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

 fname = "mbox-short.txt"
'''

fname = input("Enter file name: ")
try:
    fh = open(fname,'r')
except:
    print("Invalid file name")
    quit()
listLine=list()
for line in fh:
    if(line.startswith('From:')):
        listLine.append(line)

Emails=list()
for line in listLine:
    lst=line.split()
    Emails.append(lst[1])

for em in Emails:
    print(em)

print("There were",len(Emails),"lines in the file with From as the first word")

