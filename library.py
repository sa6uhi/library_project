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

