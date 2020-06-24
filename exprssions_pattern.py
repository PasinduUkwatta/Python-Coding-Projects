import re
#we can get the reguler expression by using the regex101.com
pattern =re.compile(r"([A-Za-z]).([a])")

string = 'search for inside this text'

a=pattern.search(string)

print(a.group(1))
print(a.group(2))