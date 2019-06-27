

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a if a > b else b
    else:
        return a if a < b else b


print(lesser_of_two_evens(2, 10))


def animal_crackers(string):
    words = string.split()  # if going purely by letter and ignore case, apply string.lower() before split
    return words[0][0] == words[1][0]


print(animal_crackers('Liam lamb'))
print(animal_crackers('Jim Dog'))


def makes_twenty(a, b):
    return (a == 20 or b == 20) or sum([a, b]) == 20


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
