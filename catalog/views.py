from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from .models import Book,Author,BookInstance,Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()

    num_books_containing_the = Book.objects.filter(title__icontains='the').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_containing_word_the': num_books_containing_the
    }

    return render(request,'index.html',context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book

    context_object_name = 'book_list'
    queryset = Book.objects.filter(title__icontains='the')[:5]
    book_list_template = 'catalog/book_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.filter(title__icontains='war')[:5]

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        # Create any data and add it to the context
        # context['some_data'] = 'This is just some data'
        return context
