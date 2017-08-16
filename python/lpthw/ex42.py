#!/usr/bin/env python2
# Animal is-a object
class Animal(object):
    pass

# Dog is-a Animal
class Dog(Animal):
# class Dog has-a __init__ that takes self and name parameters
    def __init__(self, name):
# from self get the name attribute and set it to name
        self.name = name

# create class named Cat is-a Animal
class Cat(Animal):
# has-a __init__ that takes self and name parameters
    def __init__(self, name):
# from self get the name attribute and set it to name
        self.name = name

# create class named Person that is-a object
class Person(object):
# has-a __init__ that takes self and name parameters
    def __init__(self, name):
# from self get the name attribute and set it to name
        self.name = name
# person has-a pet of some kind
        self.pet = None

# create class named Employee that is-a Person
class Employee(Person):
# has-a __init__ that takes self, name, and salary parameters
    def __init__(self, name, salary):

        super(Employee, self).__init__(name)
# from self take salary attribute and set it to salary
        self.salary = salary

# create class Fish that is-a object
class Fish(object):
    pass

# create class Salmon this is-a Fish
class Salmon(Fish):
    pass

# create class Halibut that is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# from mary take pet attribute and set it to satan (has-a)
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

# from frank take pet attribute and set it to rover (has-a)
frank.pet = rover

# set flipper to an instance of class Fish (is-a)
flipper = Fish()

# set crouse to an instance of class Salmon (is-a)
crouse = Salmon()

# set harry to an instance of class Halibut (is-a)
harry = Halibu()
