from django.contrib import admin
from .models import Todo
from .models import Books
from .models import Price


admin.site.register(Todo)
admin.site.register(Books)
admin.site.register(Price)


