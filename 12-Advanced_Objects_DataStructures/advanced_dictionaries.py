d = {'k1': 1, 'k2': 2}

print({x: x**2 for x in range(10)})

print({k: v**2 for k,v in zip(['a','b'], range(2))})

for item in d.items():
    print(item)

#By themselves the keys(), values() and items() methods return a dictionary view object.
key_view = d.keys()
print(key_view)

d['k3'] = 3
print(d)

print(key_view)