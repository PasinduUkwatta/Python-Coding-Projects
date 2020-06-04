print(("hi hello there"))
print(type("hi hello there"))

#we can  use three single qutes for long string like paragraphs or essays
long_string = '''

wooow

open

qwwe
'''
print(long_string)


first_name = 'pasindu'
last_name = 'thiwanka'

full_name = first_name+" "+last_name

print(full_name)


#string concatanation

print ('hello' +'pasindu')


print(type(str(100)))
#type Conversion
a =str(100)
b=int(a)
c=type(b)
print(c)

#Escape SEquence

weather = "it\'s a \"kind of\" sunny day "

print(weather)


#Formated Strings

name ='pasindu'
age = 24
print('hi '+name+' your age is '+str(age))

#we can create formated string in adding f in the start  
#this is a feature in python 3 
print(f'hi {name} . your {age} years old .')

word ="hello world"

print(word[0])
print(word[6])
print(word)

#[start:stop:stepover]
print(word[3:7])
print(word[0:11])
print(word[0:11:2])

#start from the beginig and go till the end of the array
print(word[0:])

#start from the beginig and go untill the desired point

print(word[:6])

#go from the step over

print(word[::2])

#we can use negative values to get the values from the end

print(word[-1])

#reverse the order of the string

print(word[::-1])

#we cannot reasign the part of the string

name ='pasindu'

#name[2] = 'b'
#we should declare the whole string

name ='thiwanka'
print(name)

#length function

greet ="good Morning!"

print(len(greet))
print(greet[:len(greet)])

#string methods

quote= "welcome to the python programming"
#conver all to the upper case
print(quote.upper())

#this will set the first letter captial letter
print(quote.capitalize())

#find the first occurence
print(quote.find("to"))





