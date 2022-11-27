from django.contrib import admin
from .models import *


# admin.site.register(Author)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
