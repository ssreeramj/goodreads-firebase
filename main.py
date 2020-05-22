import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from goodreads_api import get_book_details

# Use a service account
cred = credentials.Certificate('books-library-5e9cc-firebase-adminsdk-1fd4o-6952c9e454.json')
firebase_admin.initialize_app(cred)

store = firestore.client()

db = store.collection(u'books')

isbn_list = [9788172235147, 9788184000603, 9788172238476]

for isbn_number in isbn_list:
    book_name, author_name, description, num_pages, img_url, avg_rating = get_book_details(isbn_number)
    db.add({
        'name': book_name,
        'author': author_name,
        'status': description,
        'pages': num_pages,
        'img_url': img_url,
        'avg_rating': avg_rating
    })

# for doc in db.get():
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))
  
print('Data Added!!')
  