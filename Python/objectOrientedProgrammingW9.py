#Designing programs around functions (blocks of statements that manipulate date) is called the procedure-oriented way of programming.
#Organizing your program, combining data and functionality and wrapping it inside an object is called the object oriented programming paradigm.
#Classes and objects are the two main aspects of object oriented programming.
#A class creates a new "type" where objects are instances of the class.
#Variables that belong to an object or class are referred to as "fields".
#Objects can also have functionality by using functions that belong to a class.
#These functions are called "methods". Fields and methods can also be referred to as the "attributes" of a class.
#Fields are of two types: They can belong to each instance/object of the class or they can belong to the class itself.
#These are called "instance" and "class" variables respectively.
#Classes are created using the "class" keyword.

#Methods in a class have one difference to ordinary functions. They have an extra parameter at the beginning of the parameter list.
#However, you do not provide the value for the method since Python provides it automatically.
#This variable refers to the object itself and, by convention, is given the name "self".
#For example, imagine we have a class called MyClass and an instance of the class called myobject.
#The method myobject.method(arg1, arg2) is automatically converted by Python and turned into MyClass.method(myobject, arg1, arg2).
#If you have a method that takes no arguments, you still end up with one argument - "self".

#Example of simple class

class Person:
    pass  # An empty block

p = Person()
print(p)

#We create an object/instance of this class by using the name of the class followed by a pair of parenthesis.
#We also print the object itself, which tells us that we have an instance of the "Person" class in the "__main__" module.
#The computer memory address where the object is stored is also printed, and can change since Python will store an object wherever it finds space.


#Example of Methods

class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()

#The "Self" variable is included in the function definition.



#The "__init__" method is special in that it is run as soon as an object of a class is instantiated/created.
#It is useful to do any initialization (passing initial values to your object) you want to do with your object.

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()

#"Self.name" is a "name" variable that is part of the object, while the "name" variable insit the "__init__" method is a local variable.
#We do not explicitly call the "__init__" method.



#The data part (or fields) are ordinary variables that are bound to the "namespaces" of the classes and objects.
#It means that these names are valid within the context of the classes and objects only, hence why they are called "namespaces".
#There are 2 types of fields: class and object variables, which are classified depending on whether the class or the objects owns the variable repectively.
#Class variables are shared, meaning they can be accessed by all instances of that class.
#Only one copy of a class variable exists, so any changes to that variable can be seen by all other instances.
#Object variables are owned by each individual object/instance of a class.
#In this case, each object has a copy of the field and is not shared or related to the field of the same name in a different instance.

class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

#In this example, the "population" variable belongs to the class and therefore a class variable.
#The "name" variable belongs to the object since it is assigned using "self" and is therefore an object variable.
#We refer to the "population" class variable as "Robot.population" and not as "self.population".
#We refer to "name" using the "self.name" notation in the methods of the object.
#The "how_many" method actually belongs to the class and not the object.
#We can define it as either a "classmethod" or a "staticmethod". Since we refer to a class variable, we use "classmethod".
#We mark our method as a "classmethod" by using a decorator, or a shortcut to calling a wrapper function.
#Using the "@classmethod" decorator is the same as calling "how_many = classmethod(how_many)"
#Referring to variables and methods of the same object using "self" is called an attribute reference.
#We also see docstring being used for classes as well as methods.
#We can access the class docstring with "Robot.__doc__" and the method docstring as "Robot.say_hi.__doc__"
#All class members are public, unless you use a double underscore prefix, like "__privatevar". This effectively makes it a private variable.
#The convention is that any variable that is to be used only within a class/object should begin with an underscore and all other names are public.



#One of the major benefits of object oriented programming is reuse of code, and this can be achieved through the use of inheritance.
#Inheritance involves implementing a type and subtype relationship between classes.
#Imagine if we had to keep track of teachers and students.
#They share similar characteristics like name, age and address.
#They also have specific characteristics like salary, courses, fees, etc.
#You could create 2 independent classes for each type, but adding a new common charateristic to both of them quickly becomes unwieldy.
#We can instead create a common class "SchoolMember" and then have the teacher and student classes "inherit" from this class.
#This means that they will be sub-types of this type (class) and then we add specific characteristics to these sub-types.
#If we add/change any functionality in "SchoolMember", this will automatically be reflected in the subtypes as well.
#For example, we can add a new ID card field for both teachers and students by adding it to the "SchoolMember" class.
#You can also refer to a teacher or student object as a "SchoolMember" object, which can be useful for situations like counting the number of school members.
#This is called "polymorphism", where a sub-type can be substituted in any situation where a parent type is expected.
#Note how we reuse the code of the parent class and do not need to repeat it in the different classes.
#The "SchoolMember" class in this situation is known as the "base class" or "superclass".
#The teacher and student classes are "derived classes" or "subclasses".

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()

#To use inheritance, we specify the base class names in a tuple following the class name in a class definition.
#Next, we see that the "__init__" method of the base class is explicitly called using the "self" variable so we can initialize the base class part of an instance in the subclass.
#Since we are defining the "__init__" method in the teacher and student subclasses, Python will not automatically call the constructor of the base class "SchoolMember", and we will have to call it ourselves.
#If we don't define one, Python will call the constructor of the base class automatically.
#We create different implemetation for some of our methods in our subclasses, like the "tell" method.
#Python always looks up methods in the subclass first, and then checks the superclass.
#If more than one class is listed in the inheritance tuple, it is called "multiple inheritance".
