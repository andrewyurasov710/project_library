from django.urls import path
from . import views


app_name = 'lib'

urlpatterns = [
    path(route='', view=views.index, name='index'),
]

