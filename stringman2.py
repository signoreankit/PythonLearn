strObj = "Hello, we'll be having more fun"

# UPPERCASE
print(strObj.upper())

# lowercase
print(strObj.lower())

# String are immutable
# strObj[1] = 'l' is not possible
# TypeError: 'str' object does not support item assignment

strObj2 = ". Welcome to Python Programming Language."

# Concatenation
strObj3 = strObj+strObj2
print(strObj3)

strObj3 = strObj3 + " Bye For Now."
print(strObj3)
print(strObj3.upper)  # Here er didn't call the method upper(), so python will simply tell us what 'upper' is
print(strObj.upper())  # This is right way to call

# Split Method - Split the string into an array or List in python.
listObj = strObj3.split() # By default, it'll split the string based on white space, or we can give any other delimeter
                          # as an argument based on which the string will get split.
print(listObj)

listObj2 = strObj3.split('.')
print(listObj2)

#String interpolation - When concating a string with a string variable(holding a String OfCourse!)
strVar = "May the force "
strVar2 = strVar + "be with you!"
print(strVar2)
