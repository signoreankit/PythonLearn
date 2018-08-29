# Dictionary: Holds objects in key:value pair.

dict_1 = {'apple': '23', 'mango': '40', 'kiwi': '75', 'strawberry': '67'}
print(f'Our first dictionary: {dict_1}')

# Accessing value by key name
print('The price for 3 kiwis is {k} rupees.'.format(k=dict_1['kiwi']))

# Dictionaries can hold lists and other dictionaries as values.
list_2 = [23, 33, 45.33, 77]
dict_2 = {'yonex badminton': '2300', 'list_1':['a', 'v', 'c' ,'i'], 'list_2': list_2, 'dict_inner': {'a':1, 'b':2, 'c':3}}

print(f'Our dict_2 looks like: {dict_2}')

# Accessing values from dict_2
print('Accessing list_1: %s' %(dict_2['list_1']))
print('Accessing 2nd index from list_1: {}'.format(dict_2['list_1'][2]))
print(f'Accessing dicton_inner from dict_2: {dict_2["dict_inner"]}')
print(f'Accessing specific dict_inner value in dict_2: {dict_2["dict_inner"]["b"]}')
print(f'Uppercase list index 2: {dict_2["list_1"][2].upper()}')

# Accessing keys, values and items in dictionaries

#Keys
dict_keys = dict_2.keys()
print(f'dict_2 keys: {dict_keys}')

#Values
dict_values = dict_2.values()
print(f'dict_2 values: {dict_values}')

#Items: keys and values both
dict_items = dict_2.items()
print('dict_2 items: {i}'.format(i = dict_items))


