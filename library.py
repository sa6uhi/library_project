app_name = 'library'
version = '0.1.0'
is_active = True
book_count = 0

print(f"{app_name},{version}")

def create_book(title, year, author, genre='Unknown'):
    book = {"title": title, "year": year, "author": author, "genre": genre, "is_read": False}
    return book

def is_classic(book):
    return book["year"] < 1950

book1 = create_book("Robinson Crusoe", 1719, "Daniel Defoe", "Adventure")

print(is_classic(book1))

library = []

def add_book(book):
    library.append(book)

def remove_book(title):
    for book in library:
        if book["title"] == title:
            library.remove(book)
            return
    print(f"Book {title} not found")

def all_genres():
    genres = set()
    for book in library:
        genres.add(book["genre"])
    return genres

classic_books = [book["title"] for book in library if is_classic(book)]

authors = [book["author"] for book in library]

def book_iterator(genre_filter=None):
    for book in library:
        if genre_filter is None or book["genre"] == genre_filter:
            yield book

import json

def save_library(filename="file.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(library, file, indent=2)

try:
    with open("file.json", "r", encoding="utf-8") as file:
        library = json.load(file)
except FileNotFoundError:
    print("No existing library found, starting with an empty library.")