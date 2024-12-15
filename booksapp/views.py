from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from booksapp.models import BookModel
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
import os


def booklist_view(request):
    books = BookModel.objects.all()
    title = 'Book List'
    q = request.GET.get('q')
    if q:
        books = books.filter(title__icontains=q, author__icontains=q)
        
    return render(request, 'book_list.html', context={'books': books, 'title': title})

def booklist_detail_view(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    
    if book:
        return render(request, 'book_detail.html', context={'book': book, 'title': book.title})
    else:
        raise Http404("Book not found")

@login_required
def download_book_view(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    
    # Получение пути к файлу
    file_path = book.file.path  # Используем .path для FileField

    # Проверка существования файла
    if not os.path.exists(file_path):
        raise Http404("File not found")

    # Открытие файла и подготовка ответа
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response
