from collections import OrderedDict

# Retains order of dictionary. From Python 3.7+ this is done as standard by regular dict.
# For backwards compatibility, OrderedDict should be used to ensure code runs the same on 2.7 vs 3.6/7

#normal dict
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print(d)
for k,v in d.items():
    print(k, v)

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

#maintains inserted order
for k,v in d.items():
    print(k, v)

d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d1 == d2) #True

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2) #False
