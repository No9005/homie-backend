from collections.abc import Iterable

from django.db import models
from django.utils.translation import gettext_lazy as _


class BankAccount(models.Model):
    name = models.CharField(
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

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: str | None = None,
        update_fields: Iterable[str] | None = None,
    ) -> None:
        self.IBAN = ("").join([self.IBAN[:3], self.IBAN[-2:]])
        return super().save(force_insert, force_update, using, update_fields)
