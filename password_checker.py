import re
#password must contain at least 8 chractors
#any chartor,number or define symbols are allowed
pattern = re.compile(r"^([a-zA-Z0-9@*#$]{8,})$")

password1 ='Pa$$w0rd'
password2 ='pass'

check1=pattern.fullmatch(password1)
check2=pattern.fullmatch(password2)

print(check1)
print(check2)