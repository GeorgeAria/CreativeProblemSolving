#Reusing functions from other programs that you write can be done with modules.
#Modules can be literally another class, or can be modules written in the C programming language
#Modules can be imported by other programs. This is how we use standard library modules.
#In this example, we import the "sys" module using the "import" statement.
#"Import" tells Python that we want to use this module
#The "sys" module contains functionality related to Python's interpreter and its environment, or the "SYStem".
#Python then looks for the "sys" module, but since it is a built-in module, Python knows where to find it.
#If the module is not a built-in module(compiled module), it will look in the "sys.path" variable.
#If found, all the statements in the body of the module are run and it will be made available to you.
#The "sys.argv" variable is a list of strings that contain the list of command line arguments, also known as the arguments passed to your program through the command line.
#If running the program through the command line, any arguments after "python" will be stored in the "sys.argv" variable
#In this case, if we had "python modulesW9.py we are", "pythonW9.py" would be "sys.argv[0]", "we" would be "sys.argv[1]" and "are" would be "sys.argv[2]"
#The "sys.path" variable contains the list of directory names where modules are imported from.
#Note that the first string in the "sys.path" variable is empty, indicating that the current directory is also part of "sys.path".
#This means you can import modules from your current directory.
#Otherwise, you have to place the module in one of the directories listed on the "sys.path" variable.

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')



#Importing a module in Python is a costly affair.
#To help make programs load faster, Python creates "byte-compiled" files with the extension .pyc, which is an intermediate form Python transforms a program into.
#These .pyc files are usually created in the same directory as the corresponding .py file.


#To directly import the "argv" variable from the "sys" module, your import statement can be "from sys import argv" (The from...import statement).
#In general, avoid using the "from...import" statement and use the "import" statement instead.

from math import sqrt
print("Square root of 16 is", sqrt(16))



#The "__name__" variable of a module helps us determine whether a module is being used by itself or if is being used by another module.
#If the module is being used by itself, Python will insert "__name__ = __main__".
#This allows any code that contains the "if __name__ == __main__" to be run.
#If the module is imported, then "__name__ = __(name of module)__", and the "if" statement above will not be run as a result.

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')



#For a module named "mymodule.py"

def say_hi():
    print('Hi, this is mymodule speaking.')

__version__ = '0.1'

#For a module name "mymodule_demo.py"
import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)

#For a module named "mymodule_demo2.py"
#Note that if this module had a "__version__" variable, it would clash with the "mymodule __version__" variable
#It is best to just "import" and not use the "from...import" statement
from mymodule import say_hi, __version__

say_hi()
print('Version', __version__)

#There is also "from mymodule import *"
#This imports all public names, like "say_hi()", but not the "__version__" variable since it starts with two underscores
#It is not recommended to use it.


#The built-in "dir" function returns the list of names defined by an object.
#If the object is a module, it will return a list of functions, variables and classes defined in the module.

$ python
>>> import sys

# get names of attributes in sys module
>>> dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']
# only few entries shown here

# get names of attributes for current module
>>> dir()
['__builtins__', '__doc__',
'__name__', '__package__', 'sys']

# create a new variable 'a'
>>> a = 5

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys', 'a']

# delete/remove a name
>>> del a

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']



#Packages are folders of modules with a special "__init__.py" file that tells Python that the folder is special because it contains Python modules.