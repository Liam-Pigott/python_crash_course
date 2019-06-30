def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]
for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Liam', 'Chloe', 'Ben']

# pass the function to map rather than executing with (), map does this for us
print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]

list(filter(check_even, my_nums))

for n in filter(check_even, my_nums):
    print(n)

# lambda intended to only be used once, anon functions
lambda num: num ** 2

# define lambda within map as it only needs to be used once rather than taking space defining some function
print(list(map(lambda num: num ** 2, my_nums)))

for n in filter(lambda num: num % 2 == 0, my_nums):
    print(n)


map(lambda name: name[0], names)
