from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title one", "author": "Author One", "category":"Science"},
    {"title": "Title Two", "author": "Author Two", "category":"Science"},
    {"title": "Title Three", "author": "Author Three", "category":"History"},
    {"title": "Title Four", "author": "Author Four", "category":"Maths"},
    {"title": "Title Five", "author": "Author Five", "category":"Maths"},
    {"title": "Title Six", "author": "Author Two", "category":"Maths"}
]

# get 
@app.get('/books')
async def read_all_books():
    return BOOKS


#query parameter
@app.get('/books/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# path parameter
@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"Message": "Book Not Found"}


# path parameter with query parameter

@app.get('/book/{book_author}/')
async def read_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and  book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


#post
@app.post('/books/create_books')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


#put 

@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

#delete 

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


#assignment

@app.get("/books/by_author/{author}")
async def read_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return