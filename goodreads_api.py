from config import key, secret

KEY, SECRET = key, secret

from goodreads import client
gc = client.GoodreadsClient(KEY, SECRET)

def get_book_details(isbn):
    book = gc.book(isbn=isbn)

    # print(f'Name: {type(book.title)}')
    # print(f'Author: {type(str(book.authors[0]))}')

    return book.title, str(book.authors[0]), book.description, str(book.num_pages), book.image_url, book.average_rating

    # print(f'Description: {book.description}')
    # print(book.series_works)
# get_book_details()
