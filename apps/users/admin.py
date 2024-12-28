from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "first_name", "last_name", "is_verified")
    search_fields = ("email", "username", "first_name", "last_name")
    list_filter = ("is_verified", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password", "username")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "avatar",
                    "birth_date",
                    "phone",
                    "gender",
                    "region",
                    "district",
                    "address",
                    "vip_expired_at",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
