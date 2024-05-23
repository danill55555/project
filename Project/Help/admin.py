from django.contrib import admin

# Register your models here.
from .models import User, Role, Department, Category, Status,  Task

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'phone', 'role', 'department']
    list_display_links = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'phone', 'role', 'department']
    list_filter = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'phone']
    search_fields = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'phone']

admin.site.register(User,UserAdmin)

admin.site.register(Role)

admin.site.register(Department)

admin.site.register(Category)

admin.site.register(Status)

admin.site.register(Task)