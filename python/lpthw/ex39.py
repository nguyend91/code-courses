#!/usr/bin/env python2
# creating a mapping of states to abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
print states
# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
print cities
print raw_input("Enter to create additional cities")
# add some more cities
cities['NY'] = 'New York City'
cities['OR'] = 'Portland'
print cities
# print some of the cities
print raw_input("Enter to print NY & OR cities")
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
# print some of the states abbreviations
print raw_input("Enter to print Michigan & Florida abbreviations")
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
# print city and abbreviation
print raw_input("Enter to print Michigan & Florida cities and abbreviation")
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
# print every states abbreviation
print raw_input("Enter to print all states abbreviation")
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
# print every city in state
print raw_input("Enter to print all of the cities in the state.")
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
# doing both at the same time
print raw_input("Enter to print state, abbreviation, and city")
for state, abbrev, in states.items():
    print "%s state is abbreviated %s and has city %s" % (
    state, abbrev, cities[abbrev])
# safely get a abbreviation by state that might not be there
print raw_input("Enter to see if Texas might be on the list")
print '-' * 10
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
