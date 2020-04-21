#author deepak kumar jha

'''
program to find 10 mostly used word in a given file

'''

hand=input("Enter file name : ")
try:
    fhand=open(hand,'r')
except:
    print("Invalid File Name ")
    quit()

counts=dict()
for line in fhand:    #creating dictionary 
    words=line.split()     #splitting line into word
    for word in words:
        counts[word]=counts.get(word,0)+1    # putting word value

lst=list()
for key,val in counts.items():    # creating touple using dictionary 
    newtpl=(val,key)
    lst.append(newtpl)

lst=sorted(lst,reverse=True)   #sorting touple list in reverse order

print("10 Most used word in file",hand," is\n")
for val,key in lst[:10]:
    print(key,val)


