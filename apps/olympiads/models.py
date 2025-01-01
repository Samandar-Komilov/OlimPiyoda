from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Olympiad(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"), null=False, blank=False)
    description = models.TextField(verbose_name=_("Description"), null=False, blank=False)
    owner = models.ForeignKey("users.User", on_delete=models.SET_NULL, verbose_name=_("Owner"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    start_time = models.DateTimeField(verbose_name=_("Start time"), null=False, blank=False)
    end_time = models.DateTimeField(verbose_name=_("End time"), null=False, blank=False)
    cost = models.IntegerField(verbose_name=_("Cost"), default=0, null=False, blank=False)
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    is_ongoing = models.BooleanField(default=False, verbose_name=_("Is ongoing"))

    class Meta:
        verbose_name = _("Olympiad")
        verbose_name_plural = _("Olympiads")

    def __str__(self):
        return f"<Olympiad(title={self.title})>"
