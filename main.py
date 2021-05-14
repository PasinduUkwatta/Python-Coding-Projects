test_str = "(7, 8, 9)"

# printing original string
print("The original string is : " + test_str)
print(type(test_str))

# Convert Tuple String to Integer Tuple
# Using eval()
res = eval(test_str)

# printing result
print("The tuple after conversion is : " + str(res))
print(type(res))

t = (1, 2, 3)
print(type(t))
i = ''.join(str(x) for x in t)
print(int(i))

print(type(int(i)))

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)