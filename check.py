# implementing try and catch 
# author: Deepak kumar jha 

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1

print(istr)