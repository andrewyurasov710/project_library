from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'n1': len(Book.objects.all()),
        'n2': len(Author.objects.all()),
        'n3': len(Genre.objects.all()),
    }
    return render(request, template_name='lib/index.html', context=context)


def book_list(request):
    context = {
        'books': Book.objects.order_by('title'),
    }
    return render(request, template_name='lib/book_list.html', context=context)


def book_detail(request, pk):
    context = {
        'book': Book.objects.get(pk=pk),
    }
    return render(request, template_name='lib/book_detail.html', context=context)


def author_list(request):
    context = {
        'authors': Author.objects.order_by('surname', 'name'),
    }
    return render(request, template_name='lib/author_list.html', context=context)


def author_detail(request, pk):
    context = {
        'author': Author.objects.get(pk=pk),
    }
    return render(request, template_name='lib/author_detail.html', context=context)


def genre_list(request):
    context = {
        'genres': Genre.objects.all(),
    }
    return render(request, template_name='lib/genre_list.html', context=context)


def add_comment(request):
    book_id = request.POST.get('book_id')
    book = Book.objects.get(pk=book_id)
    text = request.POST.get('text')
    author = request.POST.get('author')
    if text and author:
        new_comment = Comment(text=text, author=author, book_id=book_id)
        new_comment.save()
    return HttpResponseRedirect(book.url())
