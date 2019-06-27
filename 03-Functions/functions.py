# help quickly returns brief docs, otherwise check docs https://docs.python.org/3/
mylist = [1, 2, 3]
help(mylist.insert)


def name_function():
    """
    DOCSTRING: Information about the function
    Input: nothing
    Output: same as input
    :return:
    """
    print('Hello')


name_function()

help(name_function)


# can provide defaults in parameter definition
def say_hello(name='NAME'):
    print('Hello ' + name)


say_hello('liam')
say_hello()


def return_hello(name='NAME'):
    return 'Hello ' + name


result = return_hello('Zach')
print(result)


def dog_check(string):
    return 'dog' in string.lower()


def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


print(pig_latin('Liam'))


