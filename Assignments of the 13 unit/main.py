# 1
#* : Create a class.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

#* : Create an object.
book1 = Book("Origin", "Dan Brown", 542)
book2 = Book("Still Alice", "Lisa Genova", 188)

#* : Print title of book1 and author of book2.
print(f"The one book's title is: {book1.title}")
print(f"The two book's author is: {book1.author}")
