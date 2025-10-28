import time
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
print("-"*20)
print()

# 2
class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

task1 = Task("Review snytax", "Review how to create a class and an object", "2025-10-25", "incomplete")
print(task1.title)
print(task1.description)
print(task1.due_date)
print(task1.status)
print("-"*20)
print()

#! Solving the problem when we have too many objects.
class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def display_task(self):
        print("Title:", self.title)
        print("Description", self.description)
        print("Due date:", self.due_date)
        print("Status:", self.status)

    def change_status(self):
        self.status = "Complete"

task1 = Task("Review snytax", "Review how to create a class and an object", "2025-10-25", "Incomplete")
task1.display_task()
task1.change_status()
time.sleep(3)
print("After a while ....")
time.sleep(3)
print("\n*** Change Status ***\n")
task1.display_task()
print("-"*20)
print()

# 3
#* HomeWork

class Movie:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre

    def display_movie(self):
        print(f"""
Title: {self.title}
Director: {self.director}
Release Year: {self.year}
Genre: {self.genre}
""")
        
    def change_director(self, new_director):
        self.director = new_director

movie1 = Movie("Inception", "Christopher Nolan", "2010", "Sci-Fi")
movie2 = Movie("The Godfather", "Francis Ford Copola", "1972", "Crime")
movie3 = Movie("Parasite", "Bong Joon-ho", "2019", "Thriller")

print("------- MOVIES LIST --------")
movie1.display_movie()
movie2.display_movie()
movie3.display_movie()

print("\nChanging Movie Directors ....\n")
time.sleep(4)
movie1.change_director("Shokry Sarhan")
movie2.change_director("Ahmed Mazhar")
movie3.change_director("Ismail Yassin")
movie1.display_movie()
movie2.display_movie()
movie3.display_movie()
print("-"*20)
print()