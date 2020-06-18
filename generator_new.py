def gen_func(num):
    for i in range(0, num, 2):
        yield (i * 3 + 2)


for item in gen_func(20):
    print(item)

# in this we always get a single object
# we need to loop through the func to get the whole output
