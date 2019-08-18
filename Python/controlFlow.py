#There are 3 types of control flow statements: if, for and while

#Example of "if" statement
number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.

number = 23
running = True


#Example of while loop
while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here

print('Done')



#The for..in statement iterates through a sequence of objects
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')
#The range function returns a sequence of numbers starting from the first argument and ending before the second argument
#Our example gives us [1,2,3,4]
#A third argument can be added which determines the step count. By default, it is 1.
#If we were to say range(1,5,2), it would return [1,3]


#Example of break
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
#The len function returns the length of the string given as an argument

#Example of continue
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')