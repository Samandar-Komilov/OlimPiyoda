from django.contrib import admin

from apps.common.models import District, Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")
    list_filter = ("name", "code")


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "region")
    search_fields = ("name", "code", "region")
    list_filter = ("name", "code", "region")
