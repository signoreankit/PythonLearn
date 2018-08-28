my_list = [1,2,3]
print(my_list)

my_list = ['Ankit', '23', 'Empty']
print(my_list)

# Length of a list - how many objects is in it?
list_length = len(my_list)
print(f'Length of the list is {list_length}') # f-string style
print('This is how my list looks: {l}'.format(l=my_list))  # .format() style

# List indexing
print(f'object at index 3 is: {my_list[2]}')

# List slicing
print(f'Last 2 objects of list are: {my_list[1::]}')

# List reverse
my_list_reverse = my_list[::-1]
print('Reverse of my_list={l} is my_list_reverse={r}'.format(l=my_list, r=my_list_reverse))

#List Concatenation
list_A = ['Hey', 'Wassup', ',']
list_B = ["It's", 'been', 'a', 'while']

list_Concat = list_A + list_B

print(f'List A = {list_A}\nList B = {list_B}\nList [A+B] = {list_Concat}')

# List Mutability
list_Concat[1] = list_Concat[1].upper()
print('List_Concat can change! = {}'.format(list_Concat))

# List Append: At the end of the list, and it only takes one argument
list_Concat.append(['.','Talkin\'','\'bout', 'is', 'not', 'my', 'style']) #appending a list to a list [[]]
print('Appending a list at the end of a list: ',list_Concat)

# List pop, Removing an object or element from the list: By default removes the last item
popped_item = list_Concat.pop()
print('The popped item is %s and the List after popped item is %s' % (popped_item, list_Concat))

# Removing List item based on index
popped_item2 = list_Concat.pop(2)
print('Popped item is \'%s\' which was at index 2 and now our list looks like this: %s' % (popped_item2, list_Concat))

# List sorting using sort() method
list_char = ['f', 't', 'e', 'a', 's', 'p', 'o', 'r', 't', 's']
list_num = [2,4,6,78,9,0,1,1,1,1,4,67,8]

list_char.sort()
list_num.sort()
print(f'Sorted list_char is: {list_char}')
print(f'Sorted list_num is: {list_num}')

# Reverse a list using reverse()

list_char.reverse()
print('Reverse of sorted char list is: {sc}'.format(sc = list_char))

list_num.reverse()
print('Reverse of sorted char list is: {sn}'.format(sn = list_num))
