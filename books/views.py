from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import  Book


class BookListView(generic.ListView):

    model = Book
    paginate_by = 2
    template_name = 'books/book_list.html'
    context_object_name = 'books'



class BookDetailView(generic.DetailView):

    model = Book
    template_name= 'books/book_detail.html'
    context_object_name = 'books'


class BookCreate(generic.CreateView):

    model= Book
    fields= ['title','authors','content','price','cover']
    template_name = 'books/book_create.html'

class BookUpdate(generic.UpdateView):

    model= Book
    fields=['title','authors','content','price']
    template_name='books/book_update.html'



class DeleteView(generic.DeleteView):

    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
