############################
#     ADVANCED NUMBERS     #
############################

print(hex(12))
print(bin(1234))
print(bin(128))
print(bin(1024))

print(2**4 == pow(2,4))
print(abs(-13245))

print(round(3.1))
print(round(3))
print(round(3.9))

print(round(3.141592, 2))

############################
#     ADVANCED STRINGS     #
############################

s = 'hello world'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.count('o'))
print(s.find('o'))

print(s.center(20, 'z')) # zzzzhello worldzzzzz

print('hello\thi')
print('hello\thi'.expandtabs())

s = 'hello'
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isspace())
print(s.istitle())
print(s.endswith('o'))
print(s.split('l')) # ['he', '', 'o']
print(s.partition('l')) # ('he', 'l', 'lo')