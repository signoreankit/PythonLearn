#Sets - Unordered collections of unique elements

# To Define Set
set_1 = set()

# To add element to a set
set_1.add('Ankit')
set_1.add('Ankit')  # It wont take duplicate items. Try it!
set_1.add('Dell Xps 15')
set_1.add('Python 3.6')
set_1.add('Machine Learning')

print("Set_1: ", set_1)


# Casting a list with duplicate items into Set - To get only unique values, It can be unordered.
list_toCast = [1, 1, 1, 3, 3, 3, 3, 2, 2, 2, 2, 2]
new_set = set(list_toCast)
print('Our list is: {l}\nOur set from that list is: {s}'.format(l = list_toCast, s = new_set))