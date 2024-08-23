from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)

# Logging in and using the site
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site