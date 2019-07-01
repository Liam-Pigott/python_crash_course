class Animal:

    def __init__(self):
        print('Animal created!')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()


# Inheritance

class Dog(Animal):

    def __init__(self):
        # create instance of Animal class when creating an instance of dog
        Animal.__init__(self)
        print('Dog created')

    # override method from Animal class
    def who_am_i(self):
        print('I am a dog!')

    # can add extra methods that aren't in the Animal class
    def bark(self):
        print('Woof!')


mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()


# Polymorphism

class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'


indie = Dog('Indie')
felix = Cat('Felix')

print(indie.speak())
print(felix.speak())

for pet in [indie, felix]:
    print(type(pet))
    print(type(pet.speak()))


def pet_speak(pet):
    print(pet.speak())


pet_speak(indie)
pet_speak(felix)


# Abstract class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # throw an error
        raise NotImplementedError('Subclass must implement this abstract method')


class Dog(Animal):
    def speak(self):
        return self.name + ' says woof!'


class Cat(Animal):
    def speak(self):
        return self.name + ' says meow!'


fido = Dog('Fido')
pushkin = Cat('Pushkin')

print(fido.speak())