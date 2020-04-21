#author deepak kumar jha  quiz problems

def thing():
    print('Hello') 

print('There')


x = 'banana'
y = max(x)
print(y)

def func(x) :
    print(x)

func(10)
func(20)

def stuff():
    print('Hello')
    return
    print('World')

stuff()

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')


def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

x = '40'
y = int(x) + 2
print(y)

x = 'From marquard@uct.ac.za'
print(x[8])

print(x[14:17])

print(len('banana')*7)

greet = 'Hello Bob'

print(greet.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])