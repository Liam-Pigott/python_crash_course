# volume of a sphere
def vol(rad):
    return (4.0 / 3) * 3.14 * (rad ** 3)


def range_check(num, low, high):
    if num in range(low, high):
        print(f'{num} in the range')
    else:
        print('Not in range')


range_check(5, 2, 7)


def range_bool(num, low, high):
    return num in range(low, high)


print(range_bool(3, 1, 10))


def up_low(string):
    upper = 0
    lower = 0
    for c in string:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        else:  # when char isn't a letter
            pass
    print(f'Number of uppercase letters is {upper}')
    print(f'Number of lowercase letters is {lower}')


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


def unique_list(numlist):
    unique = []
    for num in numlist:
        if num not in unique:
            unique.append(num)
    return unique


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


def multiply(numlist):
    total = numlist[0]
    for num in numlist:
        total *= num
    return total


print(multiply([1, 2, 3, -4]))


def palindrome(s):
    return s == s[::-1]


palindrome('nursesrun')

import string


def is_pangram(string, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(string.lower())


print(is_pangram("The quick brown fox jumps over the lazy dog"))
