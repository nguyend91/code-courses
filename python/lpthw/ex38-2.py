#!/usr/bin/env python2
from sys import exit

items = "Pen Apple Applepen Pen Pineapple Pineapplepen Penpineapple-applepen"
arrange = items.split(' ')

print "How many items do we have in our possession?"
print raw_input("Enter to continue. CTRL+C to exit.")
print arrange

if 10 == len(items):
    print "10 is plenty."
else:
    print "We need about 10 items."

more_items = ["Orange", "Banana", "Mango", "Peach", "Strawberries", "Blueberries"]

print raw_input("Enter to go shopping. CTRL+C to abandon task.")
print more_items
print raw_input("Enter to gather items. CTRL+C to run out of the grocery store.")

while len(arrange) != 10:
    count = more_items.pop()
    print "Adding ", count
    arrange.append(count)
    print "There are %d items now." % len(arrange)

print arrange
