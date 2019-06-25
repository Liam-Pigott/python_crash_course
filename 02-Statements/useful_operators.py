mylist = [1, 2, 3]

for num in range(10):
    print(num)

# start 3 until 10 in steps of 2
for num in range(3, 10, 2):
    print(num)

print(list(range(0, 10, 2)))


for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

# does index count as tuples
word = 'abcde'
for item in enumerate(word):
    print(item)

for index, letter in enumerate(word):
    print(f'letter {letter} is at index {index}')

# zips lists together as far as the length of the shortest list
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c']
for item in zip(mylist1, mylist2):
    print(item)

print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])

print('mykey' in {'mykey': 123})

d = {'mykey': 123}
print(123 in d.values())

print(f'min of mylist1 is {min(mylist1)}')
print(f'max of mylist1 is {max(mylist1)}')

from random import shuffle
from random import randint

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist)
print(mylist)
shuffle(mylist)
print(mylist)

print(randint(0, 100))

input = int(input('Enter a number here: '))
print(input)
