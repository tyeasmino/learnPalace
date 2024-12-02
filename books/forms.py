from django import forms
from .models import BookCategoryModel, BookModel, CommentModel

class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategoryModel
        fields = '__all__'
    

class BookDetailsForm(forms.ModelForm):
    class Meta: 
        model = BookModel
        fields = '__all__' 
    

class CommentsForm(forms.ModelForm):
    class Meta: 
        model = CommentModel
        fields = ['comment', 'book_rating'] 