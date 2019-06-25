# if, elif and else

if True:
    print("It's True")
else:
    print("False")

loc = 'Bank'

if loc == 'Work':
    print('Time to work')
elif loc == 'Bank':
    print('Money maker')
else:
    print("I don't know")

name = 'Liam'
if name == 'Liam':
    print("Hello Liam")
elif name == 'Dan':
    print('Hi Dan')
else:
    print("What's your name?")

# For Loops

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print(num)

for num in mylist:
    if (num % 2 == 0):
        print(f'Even number: {num}')
    else:
        print('Odd number: {}'.format(num))

list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(f'The total sum of mylist is {list_sum}')

my_string = 'Hello world'
for letter in my_string:
    print(letter)

for _ in my_string:
    print('_ is used when there isn\'t any intention to use a variable in the for loop')

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(mylist))

for item in mylist:
    print(item)

# tuple unpacking
for a, b in mylist:
    print(a)
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)  # only prints keys

for key, value in d.items():
    print(value)  # prints values


# While loops

x = 0
while x < 5:
    print(x)
    x += 1
else:
    print('x is not less than 5')

# break: breaks out of current enclosing loop
# continue: goes to the top of the closest loop
# pass: does nothing

x = [1, 2, 3]

for item in x:
    pass  # good as a placeholder to code later and avoid syntax errors

my_string = 'Liam'
for letter in my_string:
    if letter == 'a':
        continue
    print(letter)

my_string = 'Liam'
for letter in my_string:
    if letter == 'a':
        break
    print(letter)

x = 5
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1