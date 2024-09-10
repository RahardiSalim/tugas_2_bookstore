from django.shortcuts import render
from .models import Product as Book

def show_main(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, "main.html", context)