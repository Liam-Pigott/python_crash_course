# GLOBAL
# name = 'Global string'


def greet():
    # ENCLOSING
    # name = 'Liam'

    def hello():
        # LOCAL
        name = 'Local name'
        print('Hello ' + name)

    hello()


greet()

x = 50


# possible but can lead to strange issues, best to re-assign global variable with something like x = func(x)
def func():
    global x  # reach out to global namespace
    print(f'X is {x}')

    # locally re-assigning a global value so functions can have an effect on global scope
    x = 200
    print(f'Changed GLOBAL variable X to {x}')
