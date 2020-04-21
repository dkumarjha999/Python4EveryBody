
#author deepak kumar jha
'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest 
number of mail messages. The program looks for 'From ' lines and takes the second word of those
lines as the person who sent the mail. The program creates a Python dictionary that maps the 
sender's mail address to a count of the number of times they appear in the file.After the
dictionary is produced,the program reads through the dictionary using a maximum loop to find 
the most prolific committer.

'''
# fname= mbox-short.txt

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

emailSent=dict()
for em in Emails:
    emailSent[em] = emailSent.get(em,0) + 1

maxval=max(emailSent.values())
for key,val in emailSent.items():
    if val==maxval:
        print(key,val)



