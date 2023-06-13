from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile

# Register your models here.


class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display = ('email', 'username', 'first_name', 'last_name','role', 'is_active', 'date_joined')
    ordering = ('-date_joined',)    # default sort by date_joined descending.

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)