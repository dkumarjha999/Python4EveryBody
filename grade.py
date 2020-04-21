
#author deepak kumar jha
'''

3.3 Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. If the score is between 0.0 and 1.0,
 print a grade using the following table:

Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. 
For the test, enter a score of 0.85.

'''


grade=input("Enter grade:")
try:
    gr=float(grade)
except:
    print("Error variable type")
    quit()

if gr>1.0:
    print("value out of range")
    quit()
elif gr<0.6:
    print("F")
elif gr<0.7 and gr>=0.6:
    print("D")
elif gr<0.8 and gr>=.7:
    print("C")
elif gr<0.9 and gr>=0.8:
    print("B")
elif gr<=1.0 and gr>=0.9:
    print("A") 

