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