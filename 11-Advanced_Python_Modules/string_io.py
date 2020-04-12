import io

# implements an in-memory file like object.
message = 'This is just a normal string.'
f = io.StringIO(message)

#Now we have an object f that we will be able to treat just like a file. 
print(f.read())
f.write(' Second line written to file like object')
f.seek(0)
print(f.read())

f.close()