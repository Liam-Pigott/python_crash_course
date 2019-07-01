class Sample:
    pass


mysample = Sample()
print(mysample)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # special method to override what is returned by str() / print()
    # without this, would return class object and memory location
    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')


b = Book('Python Tuts', 'Jose', 200)

print(b)
print(str(b))

print(len(b))

# delete variable from memory
del b
