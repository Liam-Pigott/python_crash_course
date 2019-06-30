class Dog:
    # Class object attribute = same for any instance of the class
    species = 'Mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # methods
    def bark(self):
        print(f"Woof! My name is {self.name}")


my_dog = Dog('German Shepherd', 'Teddy')
new_dog = Dog(breed='German Shepherd', name='Indie')

print(my_dog.breed)
print(new_dog.breed)
print(new_dog.species)
new_dog.bark()


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi  # can also use Circle.pi as its value is the same for all instances

    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle()
print(my_circle.radius)
print(my_circle.get_circumference())

my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.get_circumference())
