from django.contrib import admin
from . import models

admin.site.site_header = "Добро пожаловать в панель администратора!"
admin.site.site_title = "Books_Authors"
admin.site.index_title = "admin"


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'book_id')


class BookInline(admin.TabularInline):
    model = models.Book
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_id')
    inlines = [BookInline]


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
