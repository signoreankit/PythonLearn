# String Formatting using print method

# 1 - The .format() method
print('Hello, my name is {}') # Output: Hello, my name is {}
print('Hello my name is {}'.format('Ankit')) # Output: Hello, my name is Ankit

# More Examples
print('Hello, my name is {} {}'.format('Ankit', 'Srivastava'))
print('This {1} is full of {0}.'.format('mysteries', 'universe'))  # strings can be inserted at index position
#  index 1 and index 0 in format method arguments: {1} = universe, {2} = mysteries

# More Ways -- to use keywords
print('{t} song, What does {t} {f} say, is {a}.'.format(t='the', a = 'awesome', f='fox'))

#Floor Formating

floatNum = 1723534534.434343435353535553
print('The Float num is {f:1.2f}'.format(f = floatNum))  # {value:width.precisionf}


# 2 - The f-string format, new in python 3.6, something like js es6 template string format

varName = "Bottle"
varAge = 98.987654332

print(f'This {varName} is {varAge:1.2f} years old.')  #add 'f' in the beginning and in curly braces directly use the variables

# Traditional way of using %(percentage symbol) operator in string formatting

print('This %s is used to contain water which is %d years old' % (varName, varAge))
