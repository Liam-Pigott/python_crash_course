# *args and **kwargs, arguments and keyword arguments


def my_func(a, b):
    return sum((a, b)) * 0.05


my_func(40, 60)


# *args = any number of args passed as tuple
# doesn't need to be args, just convention. * is the key part
def my_func(*args):
    return sum(args) * 0.05


print(my_func(40, 60))
print(my_func(40, 60, 80))
print(my_func(40, 60, 80, 100))


# **kwargs = any number of args passed as dictionary
def my_func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('no fruit here')


my_func(fruit='apple', veg='carrot')


# order is still important when using both args and kwargs, in this case calls to the function should pass args first
def my_func(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


my_func(10, 20, 30, fruit='orange', food='eggs', animal='dog')


def my_func(*args):
    my_list = []
    for arg in args:
        if arg % 2 == 0:
            my_list.append(arg)
    return my_list


def myfunc(string):
    x = 0
    result = ''
    while x < len(string):
        if x % 2 == 0:
            result += string[x].lower()
        else:
            result += string[x].upper()
        x += 1
    return result


print(myfunc('LiamPigott'))

