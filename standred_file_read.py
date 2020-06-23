#use of this is that we didnot need to close the file
with open('test.txt') as my_file:
    print(my_file.readlines())