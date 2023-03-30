from django.contrib import admin
from MyApps1.models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "pages", "price"];


admin.site.register(Book, BookAdmin)
