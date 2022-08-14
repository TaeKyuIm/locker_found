from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models

class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ("username", "nickname")
    list_filter = ('username', 'nickname', 'is_active', 'is_staff')
    ordering = ('-created_at',)
    list_display = ('username', 'id', 'nickname', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username','nickname')}),
        ('Permissions', {'fields': ('is_staff','is_active')}),
       
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':20,'cols':60})},
    }

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields': ('username', 'nickname', 'password1', 'password2', 'is_active', 'is_staff',)
        }),
    )


admin.site.register(CustomUser, UserAdminConfig)