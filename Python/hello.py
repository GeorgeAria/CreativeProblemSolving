msg = "Hello, World!";
print(msg);
#This is an example of a comment

#Strings can be contained in single or double quotes
"Hello"
'World'
# Triple quotes define a string that can be written in multiple lines
"""Hello
My
Friends"""

#Strings are immutable, meaning that once they are created, they can not be changed

#Format method substitutes the parts of the string with the {}  with the values you give it in the parenthesis
#The numbers in the {} are optional
age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))


#This accomplishes the same thing, but it is uglier and more error-prone
name + ' is ' + str(age) + ' years old'


#F-strings are an easy way to use name parameters
age = 20
name = 'Swaroop'

print(f'{name} was {age} years old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string


#Format allows for a couple of other things
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))


#Escape sequences allow you to use otherwise unusable characters in your string
#\' would be used to represent a single quote in your string
#\\ can be used to represent \
print('Hello, what\'s you\"re name?\\')

#Raw strings, or strings that are not specially processed, can be defined be prefacing the string with an r or R
print(r"Newlines are indicated by \n")


# We use variables to hold objects (anything used by our program is an object)
#Variables are examples of identifiers. Identifiers are names given to identify something.
#Variables can hold different kinds of data types.