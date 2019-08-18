#Creating a program that creates a backup of all important files.
#Which files are to be backed up? How are they stored? Where are they stored?
#This leads into "designing" the program and creating a list of how the program will work.

#After that, we start to create the "implementation" of our solutiion.

import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
source = ['"C:\\Users\georg\Desktop\WOD Stuff"']
# Example on Mac OS X and Linux:
#source = ['/Users/swa/notes']
# Notice we have to use double quotes inside a string
# for names with spaces in it.  We could have also used
# a raw string by writing [r'C:\My Documents'].

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
target_dir = 'C:\\Backup'
# Example on Mac OS X and Linux:
#target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

#This then leads into the "testing" phase where we find out if our program works properly.
#If it does not, we have to debug our program, which means removing bugs(errors) from our program.

#The "os.sep" variable is the directory seperator according to our operating system (i.e. / for Linux/MacOSX and \\ for Windows).
#This helps make our program portable, working across multiple systems.
#The "time.strftime()" function takes a specification like the one we provide it in our program. %Y is the year, %m is the month (as a decimal between 01 and 12) and so on.
#The string "zip_command" contains the command that we are going to execute.
#The "zip" command we use has a "-r" option, which says that the zip command should work Recursively for directories, meaning it should include all subdirectories and files.
#We then run the program through the "os.system()" function which runs the command from the system, and returns 0 if it ran successfully.

#We then head into the "operation/deployment" phase and use it wherever we want to take a backup of our files.
#Usually, first versions of programs don't work exactly as expected. It may require us to go back to the design phase or debug our program.

#We then head into the "maintenance" phase, where we make refinements to our program.
#A refinement for our program can be using the time as the name of the file in the directory, with the name of the directory being the current date.
#This allows our backups to be stored in a hierarchical manner, making it easier to manage.
#It also makes filenames shorter, and seperate directories will help us check if we made a backup for each day.

import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
source = ['"C:\\Users\georg\Desktop\WOD Stuff"', 'C:\\Code']
# Example on Mac OS X and Linux:
#source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
target_dir = 'C:\\Backup'
# Example on Mac OS X and Linux:
#target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# The name of the zip file
target = today + os.sep + now + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

#We now check if there is a directory with the current day in its name inside the main backup directory using the "os.path.exists" function.
#If it doesn't exist, we create it using the "os.mkdir" function.

#Another refinement we can make is attaching a user-supplied comment to the name of the zip archive.
#This allows us to differentiate what the backups are for.

import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

#We take in the user's ccomments with the "input" function and check that they actually entered something with the "len" function.
#If nothing is provided, we do what our previous programs have done. If a comment is supplied, we attach it to the name of the zip archive before the ".zip" extension.
#We also replace any spaces with underscores to help us manage filenames easier.


#The varuous phases of writing software include:
#1. What (Analysis)
#2. How (Design)
#3. Do It (Implementation)
#4. Test (Testing and Debugging)
#5. Use (Operation or Deployment)
#6. Maintain (Refinement)

#Software is grown, no built.