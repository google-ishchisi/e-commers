from django.contrib import admin
from .models import Accounts
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
	list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
	list_display_links = ('email', 'first_name', 'last_name')
	ordering = ('-date_joined',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Accounts, AccountAdmin)