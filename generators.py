def make_list(num):
    result = []
    for i in range(num):
        result.append(i*3)

    return result

my_list =make_list(20)
print(my_list)




def generator_function(num):
    for i in range(num):
        yield i

for item in generator_function(100):
    print(item)

print(generator_function())