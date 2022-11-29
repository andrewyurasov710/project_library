from django.urls import path
from . import views


app_name = 'lib'

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='books/', view=views.book_list, name='book_list'),
    path(route='book/<int:pk>/', view=views.book_detail, name='book_detail'),
    path(route='authors/', view=views.author_list, name='author_list'),
    path(route='author/<int:pk>/', view=views.author_detail, name='author_detail'),
    path(route='genres/', view=views.genre_list, name='genre_list'),
]


