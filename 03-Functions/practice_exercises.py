def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a if a > b else b
    else:
        return a if a < b else b


# could have used min and max i.e. return min(a,b)


print(lesser_of_two_evens(2, 10))


def animal_crackers(string):
    words = string.split()  # if going purely by letter and ignore case, apply string.lower() before split
    return words[0][0] == words[1][0]


print(animal_crackers('Liam lamb'))
print(animal_crackers('Jim Dog'))


def makes_twenty(a, b):
    return a == 20 or b == 20 or sum([a, b]) == 20


print(makes_twenty(20, 2))
print(makes_twenty(18, 2))
print(makes_twenty(200, 2))


# uppercase first and fourth letter
def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]


print(old_macdonald('macdonald'))


def master_yoda(string):
    return " ".join(string.split()[::-1])


print(master_yoda('I am home'))
print(master_yoda('We are ready'))


def almost_there(n):
    return 90 <= n <= 110 or 190 <= n <= 210


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


def has_33(nums):
    if len(nums) < 2:
        return False
    else:
        for i in range(0, len(nums) - 1):
            if nums[i] == 3 and nums[i + 1] == 3:
                return True
        return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


def paper_doll(string):
    result = ''
    for s in string:
        result += s * 3
    return result


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


def blackjack(*args):
    total = sum(args)
    if 11 in args and total > 21:
        total -= 10
    else:
        if sum(args) > 21:
            return 'BUST'
    return total


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


def summer_69(list):
    total = 0
    add = True
    for num in list:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


def count_primes(num):
    # check for 0 or 1 input
    if num < 2:
        return 0

    primes = [2]
    x = 3
    # check up until input num
    while x <= num:
        # check if x is prime, steps of 2 as even numbers aren't prime
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:  # for else statement
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


count_primes(100)
