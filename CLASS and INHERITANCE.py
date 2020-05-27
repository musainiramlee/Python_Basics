# Class is a method that is used to set a new type.


class Person:
    def __init__(self, name):
        self.name = name  # ways to define the name

    def intro(self):
        print(f'Hi there! I am {self.name}, I will be your assistant today.')

    def ask_initial(self):
        print('May I help you with your booking?')


man1 = Person('John')
man1.intro()
man1.ask_initial()

# Inheritance.
# Inheritance can be used to save a 'common' function shared by many objects


class Animal:
    def walk(self):
        print('Walking..walking.')


class Bear(Animal):
    def growl(self):
        print('Grrr..grrr')


class Rabbit(Animal):
    def hop(self):
        print('Toink..Toink')


x1 = Bear()
x2 = Rabbit()
x2.hop()
x1.walk()
x1.growl()
x2.hop()

