import re

pattern = re.compile('the')

string = 'the search inside the string'

text =(pattern.search(string))

print(text.span())
print(text.start())
print(text.end())
print(text.group())
print(pattern.findall(string))
