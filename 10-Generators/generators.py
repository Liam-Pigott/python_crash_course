
#creates list in memory through result
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

#no list in memory, just generates the values as needed through yield
def create_cubes_generator(n):
    for x in range(n):
        yield x**3

print(create_cubes(10)) #prints list
print(create_cubes_generator(10)) #generator object at memory location. Need to iterate for list or assign to list.
print(list(create_cubes_generator(10)))

for x in create_cubes(10):
    print(x)

#same as above but with smaller memory footprint
for x in create_cubes_generator(10):
    print(x)

def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b #a takes value of b, b takes value of a+b

for number in gen_fibon(10):
    print(number)


def simple_generator():
    for x in range(3):
        yield x

for number in simple_generator():
    print(number)

g = simple_generator()
print(g) # generator object
print(next(g)) #0
print(next(g)) #1
print(next(g)) #2
#print(next(g)) #stop iteration error as we have yielded all values. For loop catches this automatically.ArithmeticError

s = 'hello'
for char in s:
    print(char)

#print(next(s)) # string object is not an iterator

s_iter = iter(s)
print(next(s_iter)) #h
print(next(s_iter)) #e
print(next(s_iter)) #l