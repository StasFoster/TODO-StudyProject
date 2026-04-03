from django.contrib import admin
from .models import User, Task
# Register your models here.

@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ["name"]