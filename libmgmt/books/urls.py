from django.urls import path
from .views import (
    book_list_view,
    book_create_view,
)

app_name = 'books'
urlpatterns = [
    path('', book_list_view, name='book-list'),
    path('create/', book_create_view, name='book-create'),
]
