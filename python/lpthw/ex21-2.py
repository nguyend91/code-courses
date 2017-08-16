#!usr/bin/env python2
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

age = add(20, 25)
weight = subtract(150, 50)

print "Age is %d, and weight is %d" % (age, weight)

who = add(age, subtract(weight, 50))

print "Trying to figure out what this", who
