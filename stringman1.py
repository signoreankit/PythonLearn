strObj = "Hello, this is a string"

# Finding length of the string, SPACES are included as a part of the string.
print('String Length:', len(strObj))

# Finding index value in a string. --INDEXING
print('Index 17 holds the character \''+strObj[17]+'\'')

# Getting the last character in a string.
print('Last character in strObj is ', strObj[-1])

# Slicing the part of the string. -- SLICING
""" [start:stop:jump]
    start: Index from where we want to start the slice
    stop: Index we'll go up to (but not including it)
    jump: It is the size of the jump to take, 1:no jump"""
print('Slice1:', strObj[0:5:1])

# Slicing the whole string with jump value 2
print('JUMP = 2', strObj[::2])

# Slicing using negative indexes, From back to front
print('Slice2:', strObj[-1:-7:-1])

# Does slice return anything? Yes, a string
retString = strObj[0:-1:2]
print('Slice return is: ', retString)


# type of the slice return
print('Type of retString is:', type(retString))

# Does all of the above changes original strObj
print('StrObj is: ', strObj)  # No Change!
print('StrObj type is: ', type(strObj))

# PYTHON TRICK TO REVERSE A STRING

simpleString = "Meditation"

# WAY 1
reverseString1 = simpleString[-1::-1]
print('Reverse String1:', reverseString1)

# WAY 2
reverseString2 = simpleString[::-1]
print('Reverse String2:', reverseString2)