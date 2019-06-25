

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# elements for elements in... same as the above but a one liner
mylist = [letter for letter in mystring]
print(mylist)

numlist = [num for num in range(0, 11)]
print(numlist)

numlist = [num**2 for num in range(0, 11)]
print(numlist)

# creates list of numbers in range that are even
numlist = [num for num in range(0, 11) if num % 2 == 0]
print(numlist)

celcius = [0, 10, 20, 30, 40]
fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)

# ordering gets reversed when adding else statement, little confusing and not the prettiest
results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)

mylist = []
for x in [2, 4, 6]:
    for y in [1, 20, 3000]:
        mylist.append(x * y)

print(mylist)

mylist = [x * y for x in [2, 4, 6] for y in [1, 20, 3000]]
print(mylist)