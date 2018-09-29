from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Oauth.models import NewUser
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.
class NewUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'is_staff')


admin.site.register(NewUser, NewUserAdmin)