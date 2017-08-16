#!/usr/bin/env python2
from sys import exit

def across():
    print """
    You have made it across the quicksand fairly easily.
    Do you wish to return for your supplies?
    1. Yes
    2. No
    """
    choice = raw_input("> ")
    if "1" in choice:
        print """
        When attempting to go back for your supplies.
        The branch that was holding the rope snapped,
        and you fall in the center of the quicksand.
        Unfortunately you were unable to make it out alive.
        """
        exit(0)
    elif "2" in choice:
        print """
        You have successfully moved on to the next
        checkpoint. Congratulations!
        """
        exit(0)
    else:
        print "You have to make a choice."
        across()

def quicksand():
    print """
    You have chosen to go left, but unfortunately you
    have found yourself standing in front of a quicksand
    pit. You notice a rope connected to a branch hanging
    above the pit. What should you do?
    1. Return to the beginning
    2. Get rid of your supplies in order to use the rope
        more effectively
    3. Go through because you don't believe in quicksand
    """
    choice = raw_input("> ")
    if "1" in choice:
        print "You've decided to go back."
        start()
    elif "2" in choice:
        print """
        You are starting to unload your supplies for
        the jump.
        """
        across()
    elif "3" in choice:
        print """
        Unfortunately quicksand is real and you were
        too heavy to cross unscathed. You did not make it.
        """
        exit(0)
    else:
        print "You have to make a choice."
        quicksand()

def river():
    print """
    You have chosen to go straight, but unfortunately
    you have reached a river that spans 100 feet wide
    with a heavy current. What should you do?
    1. Cross the river in hopes the current isn't too
        strong
    2. Return to the beginning
    """
    choice = raw_input("> ")
    if "1" in choice:
        print """
        Unfortunately the current of the river was too
        strong and you were swept away, never to be
        seen again.
        """
        exit(0)
    if "2" in choice:
        print "You have decided to go back."
        start()
    else:
        print "You have to make a choice."
        river()

def mountain():
    print """
    You have chosen to go right, but unfortunately
    you have picked a trail least traveled on. The
    moutains to the right are enormous and treacherous.
    What will you do?
    1. Attempt to hike the mountains
    2. Return to the beginning
    """
    choice = raw_input("> ")
    if "1" in choice:
        print """
        You have successfully made it halfway up the
        mountain, but then suddenly you lose your
        footing and come tumbling down 100 feet from
        the bottom. You die instantly.
        """
        exit(0)
    if "2" in choice:
        print "You have decided to go back."
        start()
    else:
        print "You have to make a choice."
        mountain()

def start():
    print """
    You have traveled many miles and endured plenty
    obstacles. You have one last obstacle standing in
    your way. You're stuck at a fork in the road
    involving 3 different paths you can take. To the
    left the brush looks to be overflowing with
    vegetation. Straight ahead the path seems simple
    and paved. To the right you see a lot of trees
    as high as about 100 feet tall. Which path do
    you decide?
    1. Right
    2. Left
    3. Straight
    """
    choice = raw_input("> ")
    if "1" in choice:
        mountain()
    elif "2" in choice:
        quicksand()
    elif "3" in choice:
        river()
    else:
        print "You have to make a choice."
        start()

start()
