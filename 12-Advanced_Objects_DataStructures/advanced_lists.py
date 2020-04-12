list1 = [1,2,3]
list1.append(4)
print(list1)
print(list1.count(10))
print(list1.count(2))

x = [1, 2, 3]
x.append([4, 5])
print(x) # [1, 2, 3, [4, 5]]

x = [1, 2, 3]
x.extend([4, 5])
print(x) # [1, 2, 3, 4, 5]

print(list1.index(2))
#print(list1.index(12)) # Value error

list1.insert(2,'inserted')
print(list1) # [1, 2, 'inserted', 3, 4]

ele = list1.pop()
print(ele)
print(list1)
list1.pop(0)
print(list1)

list1.remove('inserted')
l = [1,2,3,4,3]
l.remove(3) # [1,2,4,3] removes first instnce
l.reverse()
print(l)
l.sort()
print(l)

# Assignment doesn't work the same way as with strings
x = 'hello world'
y = x.upper()
print(y) # HELLO WORLD

x = [1,2,3]
y = x.append(4)
print(y) # None . As the operation affects the list in place, result value of calling this method is actually None.
print(x) # the x.append(4) still affects the list x even if it looks like it should be assigned to y instead.