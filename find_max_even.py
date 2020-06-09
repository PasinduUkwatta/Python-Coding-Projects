
#find the maximum even number from the list
my_list = [18, 93, 2, 100, 87, 29, 2, 2, 33]
even_list =[]

def highest_even(list):
   
    for items in my_list:
        if items % 2 == 0:
            even_list.append(items)

    return max(even_list)


print(highest_even(my_list))