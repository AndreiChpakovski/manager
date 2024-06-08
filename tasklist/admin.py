from django.contrib import admin

from .models import Manager, Task, Comment

# Register your models here.

admin.site.register(Manager)
admin.site.register(Task)
admin.site.register(Comment)
