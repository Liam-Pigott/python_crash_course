########################################
#                                      #
#               Lists                  #
#                                      #
########################################

my_list = [1, 2, 3]
my_list = ['String', 100, 523.3]

list_len = len(my_list)
print(list_len)

print(my_list[0])
print(my_list[1:])

another_list = [2, 'list']
print(my_list + another_list)

another_list[-1] = another_list[-1].upper()
print(another_list[-1])

another_list.append(42)
print(another_list)
another_list.append(43)
print(another_list)
another_list.pop()
print(another_list)

popped_item = another_list.pop()
print(another_list)

# pop removes the last element of a list unless a specific index is given
another_list.pop(0)
print(another_list)

new_list = ['a', 'f', 'x', 'l', 's']
num_list = [2, 8734, 34, 23, 42, 89, 0, 33, 42]

new_list.sort()
print(new_list)

# returns None as the function doesn't return anything in this scenario
print(num_list.sort())
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

########################################
#                                      #
#          Dictionaries (MAPS)         #
#                                      #
########################################

my_dict = {'key1': 'val1', 'key2': 'val2'}
print(my_dict['key2'])

prices_lookup = {'python': 12.99, 'html': 0.1, 'scala': 42}
print(prices_lookup['scala'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 'insideVal'}}
print(d['k3']['insideKey'])

# add to map
d['k4'] = 100
print(d)

d['k1'] = 456
print("Keys: {}".format(d.keys()))
print(f"Values: {d.values()}")
print("Items: {items}".format(items=d.items()))

########################################
#                                      #
#           Tuples (immutable)         #
#                                      #
########################################

t = (1, 2, 3)
print(type(t))
print(len(t))

t = ('one', 2)
print(t[0])

t = ('a', 'a', 'b')
print(t.count('a'))

print(t.index('a'))

# Cannot re-assign values in tuples, used for data integrity
# t[0] = 'NEW'

########################################
#                                      #
#   Sets (Unordered Unique elements)   #
#                                      #
########################################

myset = set()
print(myset)

myset.add(1)
print(myset)
myset.add(2)
print(myset)
# won't add this as 2 already exists in the set
myset.add(2)
print(myset)

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
print(set(mylist))



########################################
#                                      #
#             Booleans                 #
#                                      #
########################################

# need to be capital
type(True)
type(False)

print(1 > 2)
print(1 == 1)

b = None
type(b)

