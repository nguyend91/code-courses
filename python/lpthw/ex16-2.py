from sys import argv

script, filename = argv

print "%r will be re-written if you wish to continue." %filename
raw_input("Press ENTER to continue, otherwise Ctrl+C to exit.")

target = open(filename, 'w')
target.truncate()

print "Now write the opening sentence."

sentence = raw_input("")

target.write(sentence)

print "This document will be closed."

target.close()
