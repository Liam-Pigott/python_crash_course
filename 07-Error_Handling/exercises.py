for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except TypeError:
        print('Cannot square this data type')

x = 5
y = 0

try:
    x / y
except ZeroDivisionError:
    print('Cannot divide by 0')
finally:
    print('All done')


def ask():
    while True:
        try:
            n = int(input('Enter a number: '))
        except:
            print('Please try again! \n')
        else:
            break
    print('Your number squared is: ')
    print(n ** 2)


ask()
