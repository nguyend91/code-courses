#!/usr/bin/env python2

from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(from_file)
from_file.read()

print "%d bytes long" % len(from_file)

print "Exists? %r" % exists(to_file)

raw_input()

open(to_file, 'w')
to_file.write(from_file)

from_file.close()
to_file.close()
