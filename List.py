li1 =[1,2,3,4,5,5,6]
li2 =['a','c','f','t','d','d','s']
li3=[1,'e','fe' ,True]

#Data Structure

shopping =['suger','rice','flour','milk']

print(shopping[0])
print(shopping[1])
print(shopping[2])
print(shopping[3])

#list Slising
#pritn all elemnts
print(shopping[0:])


#lists are mutable, so we can change the elemnts in the list
shopping[0] ='egg'
#first two elements
print(shopping[0:2])

#elemts after first one
print(shopping[1:3])

#reerse the elemts in the list
print(shopping[::-1])

#in this we are creating the copy of the shopping list
new_cart = shopping[:]
print(new_cart)

#in this we are assigning the reference of the sopping into the new_cart2
#so when we chnge a value in new_cart2 will affect to the shopping cart
new_cart2 =shopping
new_cart2[1] = 'biscuit'

print(shopping)
print(new_cart2)


numbers =[8,9,4,5,0,1,1,6,1,0,7,41,3]

print(len(numbers))

#adding
numbers.append(45)
new_list1 =numbers
print(numbers)
print(new_list1)

numbers.insert(4,100)
print(numbers)

numbers.extend([101,102])
print(numbers)


#removing

#in this pop will remove the last element
#pop we should give the index numbers
numbers.pop()
print(numbers)

#remove we should give the value
numbers.remove(41)
print(numbers)

#numbers.clear()
print(f'cleraed list :'+str(numbers))

#this will produce the index number of the selected value
print(numbers.index(100))

#in this we give the index range that we need to find
print(numbers.index(7,0,12))

letters =['a','n','b','j','k','f','l','u','a','f','a','i','o','i']

letters2 =letters.copy()
#in method will check and return the boolean value about the availability
print('o' in letters)

#count the no of selected 
print(letters.count('f'))

#we need to first sort and then print
#beacuse sort method didnt return ant value
letters.sort()
print(letters)

letters2.reverse()
print(letters2)


basket =['j','a','d','n','f','j','a','l','u','e','f','l','a']

basket.sort()
print(basket)

basket.reverse()
print(basket)

print(basket[::-1])

#this will produce the list of 0-99
print(list(range(0,100)))

#we can  use list to print the elemetns
new_sentence = ' '.join(['hi','my','name','is','pasindu'])

print(new_sentence)

