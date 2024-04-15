from django.contrib import admin
from .models import publisher,book,author
# Register your models here.
admin.site.register(publisher)
admin.site.register(book)
admin.site.register(author)