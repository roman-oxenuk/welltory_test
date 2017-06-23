from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group

from .models import User
from .forms import AccountUserChangeForm, AccountUserCreationForm


class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (
            None,
            {
                'fields': ('email', 'password')
            }
        ),
        (
            u'Personal info',
            {'fields': ('first_name', 'last_name')}
        ),
        (
            u'Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            u'Important dates',
            {'fields': ('last_login', 'created_at')}
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    readonly_fields = ('password', 'created_at',)
    list_display = ('email',)
    list_filter = ('is_active',)
    search_fields = ('email',)
    ordering = ('email',)
    form = AccountUserChangeForm
    add_form = AccountUserCreationForm


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
