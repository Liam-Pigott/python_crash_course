import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

pdb.set_trace() # opens pdb env, can check values like a watcher
# (Pdb) x + y
# *** TypeError: can only concatenate list (not "int") to list

result2 = y + x
print(result2)