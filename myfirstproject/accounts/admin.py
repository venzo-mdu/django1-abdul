from django.contrib import admin
from .models import User,Profile
from django.contrib.auth.admin import UserAdmin
from todoapp.models import Event
# Register your models here.

class UserAdmin(UserAdmin):
    list_display = ('email','username','is_active','is_staff','is_admin')
    filter_horizontal = ()
    ordering = ('email',)
    search_fields = ['email']
    list_filter = ('is_admin','email')
    fieldsets = (
       (None, {'fields': ('email', 'password','username')}),
       ('Permissions', {'fields': ('is_admin','is_staff')}),
   )
    add_fieldsets = (
       (None, {
           'classes': ('wide',),
           'fields': ('email','username','password1', 'password2',),
       }),
   )

admin.site.register(User,UserAdmin)
admin.site.register(Profile)
admin.site.register(Event)