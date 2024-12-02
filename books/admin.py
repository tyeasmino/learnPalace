from django.contrib import admin
from .models import BookCategoryModel, BookModel, BookBorrowModel, CommentModel

# Register your models here.
class BookCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}
    list_display = ['name', 'slug'] 

admin.site.register(BookCategoryModel, BookCategoryAdmin)
admin.site.register(BookModel) 
admin.site.register(BookBorrowModel) 
admin.site.register(CommentModel) 

