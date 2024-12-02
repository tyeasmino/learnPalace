from django.shortcuts import render
from books.models import BookModel, BookCategoryModel


def home(request, category_slug = None):
    bookCategory = BookCategoryModel.objects.all()
    book = BookModel.objects.all()

    if category_slug is not None:
        category = BookCategoryModel.objects.get(slug = category_slug)
        book = BookModel.objects.filter(category = category)


    return render(request, 'index.html', {'category' : bookCategory, 'book': book})