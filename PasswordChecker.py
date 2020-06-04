name = input("what is your name ?")
password =input("what is your password???")

password_lenght=len(password)
print(type(password_lenght))

star_password ="*" *password_lenght
print(star_password)

print(f'hello {name}  , your password is {star_password} , it has {password_lenght} letters long'  )