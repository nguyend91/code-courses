# unpacking variables that will be assigned soon
from sys import argv
# the 2 variables that will be entered when executing from command line
script, filename = argv
# assigning a variable to open a file
txt = open(filename)
# print the file after acknowledging it
print "Here's your file %r:" % filename
print txt.read()
print txt.close()
# file_again is a variable that allows user to enter the filename exactly in
#  order ot get it to run
print "type the filename again:"
file_again = raw_input("> ")
# it doesn't matter what is entered in the command as long as there is a
#  file that can be open and read
txt_again = open(file_again)

print txt_again.read()
print txt_again.close()
