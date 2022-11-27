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
