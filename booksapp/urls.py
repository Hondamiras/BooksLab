from django.urls import path
from booksapp.views import booklist_view, download_book_view, booklist_detail_view

app_name = 'books'

urlpatterns = [
    path('', booklist_view, name='booklist'),
    path('download/<int:pk>/', download_book_view, name='download'),
    path('<int:pk>/', booklist_detail_view, name='detail')
]