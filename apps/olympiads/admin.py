from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.olympiads.models import Olympiad


@admin.register(Olympiad)
class OlympiadAdmin(admin.ModelAdmin):
    list_display = ("title", "start_time", "end_time", "cost", "is_active", "is_ongoing")
    search_fields = ("title",)
    list_filter = ("is_active", "is_ongoing")
    fieldsets = (
        (
            None,
            {"fields": ("title", "description", "owner", "start_time", "end_time", "cost", "is_active", "is_ongoing")},
        ),
    )
