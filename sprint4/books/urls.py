from django.urls import path
from books.views import PublisherList, ChainListView, books_in_store

urlpatterns = [
path('publishers/', PublisherList.as_view()),
path("store/<slug>", books_in_store, name="store_books"),
path('chains/', ChainListView.as_view()),
]