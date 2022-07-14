from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', "firstname", 'lastname', 'date_joined', 'last_login', 'is_admin', 'is_staff',)
    search_fields = ('email', 'firstname',)
    ordering = ('is_admin', 'email')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None,
         {'fields': ('email', 'password', 'firstname', 'lastname', 'is_staff', 'is_admin', 'is_superuser', 'phone', "is_admission_taken", "is_paid" , 'admission_verify' , 'payment_verify')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'firstname', 'lastname', 'phone'),
        }),
    )


admin.site.register(Account, AccountAdmin)