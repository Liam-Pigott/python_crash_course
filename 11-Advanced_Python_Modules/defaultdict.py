from collections import defaultdict

# defaultdict is a dictionary-like object which provides all methods provided by a dictionary but takes a first argument (default_factory) 
# as a default data type for the dictionary. Using defaultdict is faster than doing the same using dict.set_default method.
# A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

d = {'k1': 1}
print(d['k1']) # 1
#print(d['k2']) # KeyError

d = defaultdict(object)
print(d['one']) # <object object at 0x006F6600>

for item in d:
    print(item)

d = defaultdict(lambda : 0)
print(d['one']) # automatically assign 0 using above lambda
d['two'] = 2
print(d) # defaultdict(<function <lambda> at 0x006A7FA0>, {'one': 0, 'two': 2})