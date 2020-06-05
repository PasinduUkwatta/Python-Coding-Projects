is_old = True
is_lisensed = True

if is_old:
    print('your old eough')

    if is_lisensed:
        print('you are lisencesd')

    else:
        print('you are not lisensed')

else:
    print('you cannot drive')

print('thnks for checking the eligibility')


num = 5
name = 'pasindu'

#in this int and string convert into the boolean  value , then the if else blocks run according to this.
print(bool(num))
print(bool(name))

if num and name :
  print(f'your name is {name} , your number is {num} ')

else :
  print('resubmit details')