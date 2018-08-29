# Tuples are just like lists except they are immutable
# They are mainly used for data integrity - cuz we can't reassign values to tuple
tuples_1 = (1, 'Ankit', [1,2,3,45,5], {'a': 1, 'b': 2})
print(f'tuples_1: {tuples_1}')

# Length of the tuple
print('Length of the tuples_1 tuple is %s' %(len(tuples_1)))

# Tuple Indexing
print('value at index 3 is {}'.format(tuples_1[3]))

# Tuple slicing
print('Some slicing in tuples_1: {}'.format(tuples_1[1::]))

# Reverse Tuple trick
print(f'Reverse of tuples_1 is: {tuples_1[::-1]}')

# Getting the count of any tuple value
a = 'Ankit'
tuple_toCount = (1, 1, 1, 1, 1, a, a, a, a, a, 'c', 'c')
print(f'Count of \'Ankit\' is: {tuple_toCount.count("Ankit")}')
print(f'Count of \'Variable a\' is: {tuple_toCount.count(a)}')

# Getting the index of any value in
tuple_toCount = (1, 1, 1, 1, 1, a, a, a, a, a, 'c', 'c')
print('Index of a in tuple_toCount is: {}'.format(tuple_toCount.index(a)))

# Differnce between list and tuple (immutability)

# List - Mutable
list_imm = [1, 2, 3, 4, 5, 6]
list_imm[2] = 'x'  # Reassigning value at any index is possible
print('List_imm: %s' % list_imm)

# Tuples - Immutable
""" tuple_imm = (1, 2, 3, 4, 5, 6)
    tuple_imm[2] = 'x'  # Reassigning value at any index is not possible
    print('tuple_imm: {}'.format(tuple_imm)"""
# Will throw an error:  'tuple' object does not support item assignment


