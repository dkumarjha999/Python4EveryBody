# author deepak kumar jha
'''
7.1 Write a program that prompts for a file name, then opens that file and reads 
through the file, and print the contents of the file in upper case. Use the file
words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt

'''

src=input("Enter file Name : ")
try:
    fhandle=open(src,'r')
except:
    print("Invalid Source File ")
    quit()
for line in fhandle:
    line=line.rstrip()     # to remove \n as it will be in every line and print also provide nextline
    print(line.upper())