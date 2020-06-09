def is_even(num):
  if(num%2==0):
    print('this is a even number')
    return True

  else:
    print('this is a odd number')
    return False


  
print(is_even(10))



#clean code
def is_odd(num):
  return num%2==1

print(is_odd(12))