def func():
    return 1

def hello():
    return "Hello!"

greet = hello
greet()

del hello
print(greet())

def hello(name='Liam'):
    print("The hello() function has been executed")

    def greet():
        return "\t This is the greet() func inside hello!"

    def welcome():
        return "\t This is the welcome() func inside hello!"

    #scope limited to within this function
    #print(greet())
    #print(welcome())

    if name == 'Liam':
        return greet
    else:
        return welcome

hello()
#greet() # not within global scope

#return function from within another function
hello_greet = hello('Liam')
print(hello_greet())

def cool():
    def super_cool():
        return "This is pretty cool!"
    
    return super_cool

some_func = cool()

print(some_func())



def hello():
    return "Hi Liam!"

def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

other(hello) #pass in raw function without executing


def new_decorator(original_func):
    
    def wrap_func():
        print("Some extra code before the original function")
        original_func()
        print("Some extra code after the original function")
    
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

# pass func_needs_decorator to function defined with @. Equivalent to 'decorated_func = new_decorator(func_needs_decorator)'
# comment out @new_decorator to remove the decoration
@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()