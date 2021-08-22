from django.contrib import admin
from .models import Category, Book, Author


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'modified_at']
    ordering = ['id']


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'code', 'price',
        'highlight', 'created_at', 'modified_at'
    ]
    ordering = ['-created_at']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'modified_at']
    ordering = ['id']


admin.site.register(Category, CategoryAdmin)

admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)
