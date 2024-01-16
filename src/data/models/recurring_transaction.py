from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from data.models.transaction import Transaction


def between_one_and_thirty_one(day: int):
    if not 0 < day <= 31:
        raise ValidationError(_("Day needs to between 0 and 31."))


class RecurringTransaction(Transaction):
    day = models.IntegerField(
        null=False,
        blank=True,
        default=1,
        validators=(between_one_and_thirty_one,),
        verbose_name=_("Day"),
    )

    class Meta:
        verbose_name = _("Recurring transaction")
        verbose_name_plural = _("Recurring transactions")

    def __str__(self) -> str:
        return str(self.day)
