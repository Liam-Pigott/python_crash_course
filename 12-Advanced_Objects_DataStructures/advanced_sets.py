s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(2)
print(s)

s.clear()

s = {1,2,3}
sc = s.copy()
s.add(4)
print(s)
print(sc)

print(s.difference(sc))

s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2) # removes all elements of s2 from s1
print(s1)

s2.discard(4)
print(s2)

s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))
print(s1)
s1.intersection_update(s2)
print(s1)

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

# check intersections
print(s1.isdisjoint(s2)) # False
print(s1.isdisjoint(s3)) # True

print(s1.issubset(s2))
print(s2.issuperset(s1))

print(s1.symmetric_difference(s2)) # {4}

print(s1.union(s2).union(s3)) # {1,2,4,5}
s1.update(s2)
print(s1)