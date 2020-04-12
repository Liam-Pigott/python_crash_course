from collections import namedtuple
#Named tuples assign a name and numerical index to a set. Kinda like quickly creating a class object

t = (1,2,3)
print(t[0])

# attributes in single string split by space
Dog = namedtuple('Dog','age breed name')

indie = Dog(age=8, breed='Indie', name='German Shepherd')

print(indie.age)
print(indie.breed)
print(indie.name)

Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur='fuzzy', claws=False, name='Kitty')

print(c)
print(c[2])