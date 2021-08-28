import random
from books.models import Publisher, Store, Book, StoreChain
import datetime

countries = ['Russia', 'USA', 'UK', 'Germany', 'Egypt', 'France', 'Australia', 'Canada', 'Norway']

PUBLISHERS = 50
BOOKS_PER_PUBLISHER = 200
STORES = 100
CHAINS = 5

def load_items():
    Publisher.objects.all().delete()
    Book.objects.all().delete()
    StoreChain.objects.all().delete()
    Store.objects.all().delete()

    publishers = [Publisher(name=f"Publisher{index}",
                            country=random.choice(countries))
                  for index in range(1, PUBLISHERS+1)]
    Publisher.objects.bulk_create(publishers)

    # create BOOKS_PER_PUBLISHER books for every publishers
    counter = 0
    books = []
    for publisher in Publisher.objects.all():
        for i in range(BOOKS_PER_PUBLISHER):
            counter = counter + 1
            books.append(Book(name=f"Book{counter}",
                              price=random.randint(50, 300),
                              issued=datetime.date(year=random.randint(1800, 2010),
                                                   month=random.randint(1, 12),
                                                   day=random.randint(1, 28)),
                              publisher=publisher))

    Book.objects.bulk_create(books)

    # create STORES stores and insert 100 books in every store
    books = list(Book.objects.all())
    for i in range(STORES):
        temp_books = [books.pop(0) for i in range(int(PUBLISHERS * BOOKS_PER_PUBLISHER / STORES))]
        store = Store.objects.create(name=f"Store{i + 1}",
                                     marginal_price=random.randint(5, 50))
        store.books.set(temp_books)
        store.save()

    stores = list(Store.objects.all())
    for i in range(CHAINS):
        temp_stores = [stores.pop(0) for i in range(int(STORES/CHAINS-1))]
        chain = StoreChain.objects.create(name=f"Chain{i+1}",
                                          best_store=random.choice(stores))
        chain.stores.set(temp_stores)
        chain.save()
