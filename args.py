#*args
#in this *func will accept any no of arguments
def super_func(*args):
  print(args)
  return sum(args)


print(super_func(1,23,4,567))
print(super_func(1,2,3,4,5,6,7))

#Rule - name , *args,default parameters , **kwargs