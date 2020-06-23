my_file = open('test.txt')
#we need to use seek to move the cursor in to the 0 index
#else cursor stay at the end pont after read the file
print(my_file.read())
my_file.seek(0)

print(my_file.read())
my_file.seek(0)

print(my_file.read())
my_file.seek(0)

my_file.close()
