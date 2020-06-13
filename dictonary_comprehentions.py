#dictonary comprehention
simple_dic ={
    'a': 1,
    'b': 2,
    'c':3
}

my_dict ={key :value*2 for key, value in (simple_dic).items() if value%2 ==0 }

print(my_dict)


my_dict_2 ={num:num*2 for num in [1,2,3] }

print(my_dict_2)