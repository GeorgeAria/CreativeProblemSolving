#Functions are reusable pieces of code
#When functions are used, we say that they are "called"
#We define a function using the "def" keyword
#We then give the function a name, or an "identifier"
#We then put parenthesis, which may have the name(s) of variable(s) inside, also known as parameters
#We finally finish with a colon
#Afterwards, the we write out the statements that are a part of the function

def say_hello():
    # block belonging to the function
    print('hello world')
# End of function

say_hello()  # call the function
say_hello()  # call the function again



#When supplying values for a function, we call them "arguments"

def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# directly pass literal values
print_max(3, 4)

x = 5
y = 7

# pass variables as arguments
print_max(x, y)


#Variables defined within a function are know as local variables
#Local variables are not related to variables outside of the function. This is the "scope" of the variable.
#All variables have the scope of the block they are declared in

x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)


#You are able to modify the variables in the top level of the program be using the "global" statement
#"Global" allows you to assign a value to a variable located outside of the function where it is used
#This is, however, not encouraged

x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)



#It is possible to make the parameters in a function optional
#Simply put the name of the variable, followed by "=" and a default value
#The default value should be constant/immutable
#NOTE: Only parameters at the end of the parameter list can be given default values

def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 5)



#If a function has many parameters, but you only want to use certain ones, you can use "keyword arguments"
#"Keyword arguments" are arguments that you supply the function that you explicitly name out
#For example, if a function has(a, b = 7, c = 10), you can say in the function call: (c = 4, a = 5)
#This makes the function easier to use since we don't have to worry about the order of the arguments
#NOTE: Make sure that any arguments you don't supply will have default values in the parameters of the function

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)


#We can also define a function that takes any number of parameters
#This is known as "VarArgs" parameters: VARiable number of ARGuments
#When a parameter name has one *, any arguments supplied will be collected into a tuple with that name
#When a parameter name has two *, any arguments supplied will be collected into a dictionary with that name

def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary    
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

total(10,1,2,3,Jack=1123,John=2231,Inge=1560)



#The "return" statement allows us to return from within a function. It will also break out of the function as well.
#Optionally, and conveniently, we can return an actual value as well.
#The "return" statement without a value is the same as "return None", meaning returning a variable of no value.
#All functions have this statement at the end unless you define you're own "return" statement.

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))




#Python has a useful feature known as "documentation strings", or "docstrings".
#"Docstrings" are useful for documenting our program better and making it easier to understand.
#The string on the first logical line of your function is the "docstring" of that function.
#The string itself is a multi-line string.
#The first line must have the first word start with a capital letter and end with a ".".
#The second line will be blank.
#The third line is reserved for detailed explanations.
#To access a "docstring" of a class, call the function and follow it with ".__doc__"
#NOTE: It is HIGHLY recommended to write "docstrings" for any non-trivial function you create


def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)


