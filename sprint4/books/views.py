from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View

from books.models import Publisher, Book, StoreChain, Store


class PublisherList(ListView):
    model = Publisher
    template_name = 'publisher_list.html'


class ChainListView(View):
    def get(self, request):
        list = StoreChain.objects.all()
        context = {'store_chains': list}
        return render(request, 'chains_list.html', context)

def books_in_store(request, slug):
    books = Book.objects.filter(store__name=slug).all()
    context = {'books': books}
    return render(request, "books.html", context)

