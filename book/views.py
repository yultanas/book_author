from django.shortcuts import render, get_object_or_404
from .models import Author, Book


def index(request):
    books = Book.objects.all()
    return render(request, 'book/book.html', {'books': books})
