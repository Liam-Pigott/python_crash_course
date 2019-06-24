
print('hello')

print('hello \nworld')

length = len('hello')


# indexing and slicing

myString = "Hello World"

# returns char at index 0
print(myString[0])

# reverse indexing (returns 'l')
print(myString[-2])


myString = 'abcdefghijk'

# prints from position 2 until the end of the string
print(myString[2:])

# returns abc as 3 is the stop index, substring up UNTIL position 3
print(myString[:3])

# returns def
print(myString[3:6])

# same as return the whole string
print(myString[::])

# returns string characters in steps of 2, acegik
print(myString[::2])

# returns string characters in steps of 2 beginning at index 2 and ending at index 7, ceg
print(myString[2:7:2])

# returns string in reverse by using negative indexing as the step
print(myString[::-1])

# Can't re-assign char values in strings as they're immutable
# name = "Liam"
# name[0] = 'S'

name = "Liam"
lastLetters = name[1:]
newName = 'K' + lastLetters

print(newName)

letter = 'z'
print(letter * 10)  # prints zzzzzzzzzz

x = 'Hello World'
# uppercase/lowercase
x.upper()
x.lower()

# split based on white space
x.split()

# splits by 'o', result includes whitespace as it's no longer the char to split by as in default
x.split('o')

print('This is a string {}'.format('INSERTED'))

print('{} {} {}'.format('Substituted', 'some', 'words'))
print('{1} {2} {0}'.format('Substituted', 'some', 'words'))

print('The {speed} {colour} {animal}'.format(animal='fox', colour='brown', speed='quick'))

result = 100/777

print("The result was {r}".format(r=result))

# value:width:floating point
print("The result was {r:1.3f}".format(r=result))
print("The result was {r:10.3f}".format(r=result))


name = "Liam"
age = 26
print(f'Hello, his name is {name}')
print(f'{name} is {age} years old')
