from django.db import models
from django.utils.translation import gettext_lazy as _


class BankAccount(models.Model):
    name = models.TextField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name=_("Name"),
    )
    IBAN = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        unique=True,
        verbose_name=_("IBAN"),
    )
    owner = models.ManyToManyField(
        to="auth.User",
        blank=False,
        verbose_name=_("Owner"),
    )

    class Meta:
        verbose_name = _("Bank account")
        verbose_name_plural = _("Bank accounts")

    def __str__(self) -> str:
        return f"{self.name} | IBAN: {self.IBAN}"
