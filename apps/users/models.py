from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.choices import GenderChoices
from apps.users.manager import UserManager


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True, verbose_name=_("Email address"), max_length=255)
    username = models.CharField(max_length=30, unique=True, verbose_name=_("Username"), null=True, blank=True)
    first_name = models.CharField(max_length=30, verbose_name=_("First name"), null=True, blank=True)
    last_name = models.CharField(max_length=30, verbose_name=_("Last name"), null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", verbose_name=_("Avatar"), null=True, blank=True)
    birth_date = models.DateField(verbose_name=_("Birth date"), null=True, blank=True)
    phone = models.CharField(max_length=30, verbose_name=_("Phone"), null=True, blank=True)
    gender = models.CharField(verbose_name=_("Gender"), choices=GenderChoices.choices, max_length=6)
    region = models.ForeignKey(
        "common.Region", on_delete=models.SET_NULL, verbose_name=_("Region"), null=True, blank=True
    )
    district = models.ForeignKey(
        "common.District", on_delete=models.SET_NULL, verbose_name=_("District"), null=True, blank=True
    )
    address = models.CharField(max_length=100, verbose_name=_("Address"), null=True, blank=True)
    # score = models.IntegerField(default=0, verbose_name=_('Score'))
    vip_expired_at = models.DateTimeField(verbose_name=_("VIP expired at"), blank=True, null=True)
    is_verified = models.BooleanField(default=False, verbose_name=_("Is verified"))

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: list = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @property
    def is_premium(self):
        return self.vip_expired_at > timezone.now() if self.vip_expired_at else False

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"User(email={self.email}, {self.get_full_name})"
