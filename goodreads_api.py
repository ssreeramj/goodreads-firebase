from goodreads import client
from config import key, secret

KEY, SECRET = key, secret

gc = client.GoodreadsClient(KEY, SECRET)


def get_book_details(isbn):
    book = gc.book(isbn=isbn)

    return book.title, str(book.authors[0]), book.description, str(book.num_pages), book.image_url, book.average_rating, book.small_image_url
