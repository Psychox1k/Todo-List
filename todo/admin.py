from django.contrib import admin

from todo.models import Tag, Task

# Register your models here.
admin.site.register(Task)
admin.site.register(Tag)
