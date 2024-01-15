from django.db import models
from django.utils.translation import gettext_lazy as _


class BankAccount(models.Model):
    name = models.TextField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name=_("Name"),
    )
    IBAN = models.TextField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_("IBAN"),
    )
    owner = models.ManyToManyField(
        to="auth.User",
        null=False,
        blank=False,
        verbose_name=_("Owner"),
    )

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("bank accounts")
