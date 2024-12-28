from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True


class Region(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    code = models.CharField(max_length=10, verbose_name=_("Code"))

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return self.name


class District(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    code = models.CharField(max_length=10, verbose_name=_("Code"))
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_("Region"))

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")

    def __str__(self):
        return self.name
