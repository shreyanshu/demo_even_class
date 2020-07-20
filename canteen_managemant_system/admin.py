from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from canteen_managemant_system.models import Cook, CookInfo, CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('profile_pic',)}),
    )


# Register your models here.
admin.site.register(Cook)
admin.site.register(CookInfo)
admin.site.register(CustomUser, CustomUserAdmin)