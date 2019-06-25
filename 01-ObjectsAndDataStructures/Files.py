import os
cwd = os.getcwd()

# Reading

myfile = open('myfile.txt')

print(cwd)

filetext = myfile.read()
print(filetext)

# prints nothing as the reader is at the end of the file from the last call to .read()
filetext2 = myfile.read()
print(filetext2)

# we need to reset the counter
myfile.seek(0)
print(myfile.read())

myfile.seek(0)
lines = myfile.readlines()

print(lines)


with open('myfile.txt') as my_new_file:
    contents = my_new_file.readlines()

print(contents)

# Writing

# Modes control access rights:
# r: read only
# w: write only
# a: append only
# r+: read and write
# w+: writing and reading (overwrite existing files or create a new file)

with open('myfile.txt', mode='w') as myfile:
    content = myfile


with open('my_new_file.txt', mode='r') as f:
    print(f.read())

# append
with open('my_new_file.txt', mode='a') as f:
    f.write('\nFourth line')

with open('my_new_file.txt', mode='r') as f:
    print(f.read())

# w creates file if it doesn't exist'
with open('jshdbfd.txt', mode='w') as f:
    f.write('This file was created with Python')



