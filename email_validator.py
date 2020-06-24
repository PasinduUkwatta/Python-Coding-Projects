import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string1='pasinduukwatta96@gmail.com'
string2='pasindu.17@itfac.mrt.ac.lk'


a =pattern.search(string1)
b =pattern.search(string2)

print(a)
print(b)

