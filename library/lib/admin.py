from django.contrib import admin
from .models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'published']
    list_filter = ['book']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'born']
    list_filter = ['surname']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['author']


admin.site.register(BookInstance)
