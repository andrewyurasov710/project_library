from django.urls import path
from . import views


app_name = 'lib'

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='books/', view=views.book_list, name='book_list'),
    path(route='book/<int:pk>/', view=views.book_detail, name='book_detail'),
]


