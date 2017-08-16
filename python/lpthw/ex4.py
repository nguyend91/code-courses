# 'cars' variable is equal to 100
cars = 100
# 'space_in_a_car' variable is equal to 4.0
space_in_a_car = 4.0
# 'drivers' variable is equal to 30
drivers = 30
# 'passengers' variable is equal to 90
passengers = 90
# 'cars_not driven' variable is going to be equal to cars less the drivers
cars_not_driven = cars - drivers
# 'cars_driven' variable is equal to the number of drivers
cars_driven = drivers
# 'carpool_capacity' variable is equal to cars_driven multiplied by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# 'average_passengers_per_car' variable is equal to passengers divided by the number of cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
