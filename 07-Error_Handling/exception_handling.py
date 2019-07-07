def add(a, b):
    print(a + b)


add(10, 20)

number1 = 20
number2 = '20'

try:
    # attempt this, carry on with script if this fails
    add(number1, number2)
except:
    print('Looks like this addition is incorrect')
else:
    print('Added correctly')

try:
    f = open('testfile', 'r')
    f.write('Writing test line')
except TypeError:
    print('There was a type error')
except OSError:
    print('OS error')
finally:
    print('finally block always runs')


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("That's not a number!")
            continue
        else:
            print("Number was provided")
            break
        finally:
            print("End of try/except block")


ask_for_int()