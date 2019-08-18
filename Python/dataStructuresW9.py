#Data structures store a collection of related data.
#There are 4 types of data structures: list, tuple, dictionary and set.

#A list is a data structure that holds an ordered collection of items.
#The items are are enclosed in square brackets so that Python knows that you are specifying a list.
#Once created, you can add, remove and and search for items on the list. Therefore, the list is a "mutable" data type, or a type that can be altered.

#A list is an example of usage of objects an classes.
#When we create a variable i and assign it the value of integer 5, we are creating an object (or instance) i of class (or type) int.
#A class can have functions/methods defined for that specific class. You can only use them when we have an object of that class.
#For example, the "append" method for our list class allows us to append an item to the end of our list.
#An example of this would be "mylist.append('an item')"
#A class can also have fields that are variables defined to be used by that class only.
#An example of this would be: "mylist.field"

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

#A list is also a sequence.
#The "end" parameter in the "print" function indicates the end of an output and to use a space instead of the usual line break.
#The "sort" method sorts the list. It affects the list itself instead of returning a modified list.
#This shows how lists are "mutable" and something like a string is "immutable".


#A tuple is used to hold together multiple objects. They are similar to lists, but without the functionality that the list class gives you.
#A tuple is "immutable" as a result, meaning you can not modify it.
#Tuples are defined by specifying items seperated by commas within an optional pair of parenthesis.
#Tuples are used in cases where a statement or user-defined function can safely assume that the collection of values in a tuple will not change.


# I would recommend always using parentheses
# to indicate start and end of tuple
# even though parentheses are optional.
# Explicit is better than implicit.
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))

#When we specify an item's position within a pair of square brackets, it is called the indexing operator.
#NOTE: An empty tuple is simply assigned to an empty pair of parenthesis. If only one item is put inside, a comma must go after the item entry, even though nothing goes after it.



#A dictionary is like an address book where you can find an address/contact info of someone by knowing only their name.
#We associate keys(name) with values(details). Note that keys are unique.
#Also, keys must be "immutable" objects, like strings, but values can be "immutable" or "mutable".
#You should only use simple objects for keys.
#An example of a dictionary: "d = {key1: value1, key2: value2}"
#Note that key-value pairs are not ordered in any manner.
#Dictionaries are instances/objects of the "dict" class.


ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])



#Sequences (which includes lists, tuples and strings) have unique features.
#They have membership tests (which are the "in" and "not in" expressions) and indexing operators, which is how we fetch a particular item in our sequence.
#They also have a "slicing" operation, which allows us to retrieve a slice of the sequence.

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

#We refer to using indexes to get individual items from a sequence as subscription operation.
#For the "splicing operation",  a third argument can be provided to indicate the step for the slicing (default is 1).

>>> shoplist = ['apple', 'mango', 'carrot', 'banana']
>>> shoplist[::1]
['apple', 'mango', 'carrot', 'banana']
>>> shoplist[::2]
['apple', 'carrot']
>>> shoplist[::3]
['apple', 'banana']
>>> shoplist[::-1]
['banana', 'carrot', 'mango', 'apple']



#A set is unordered collections of simple objects.
#They are used when the existence of an object in a collection is more important than the order or how many times it occurs.
#Using sets, we can test for membership, whether it is a subset of another set, find the intersection between 2 sets, and so on.

>>> bri = set(['brazil', 'russia', 'india'])
>>> 'india' in bri
True
>>> 'usa' in bri
False
>>> bric = bri.copy()
>>> bric.add('china')
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # OR bri.intersection(bric)
{'brazil', 'india'}


#When creating an object and assigning it to a variable, the variable only refers to the object and not the object itself.
#This means that the variable name is pointing to a certain part of your computer's memory where the object is stored.
#This is called "binding" the name to the object.

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name pointing to the same object!
mylist = shoplist

# I purchased the first item, so I remove it from the list
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object

print('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that now the two lists are different

#If you want to make a copy of a list or other sequences/complex objects, you must use the slicing operation to make a copy.



#Strings are objects that have methods that allow them to do things like checking part of a string and stripping spaces. We've already used the "format" method many times.
#Any strings used in programs are all objects of the class "str".

# This is a string object
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

