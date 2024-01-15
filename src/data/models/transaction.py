from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Transaction(models.Model):
    class CashFlowChoices(models.TextChoices):
        INCOME = "income", _("income")
        SPENDING = "spending", _("spending")

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name=_("Amount"),
    )
    user = models.ForeignKey(
        to="auth.User",
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        verbose_name=_("User"),
    )
    booking_date = models.DateTimeField(
        default=timezone.now,
        null=False,
        blank=True,
        verbose_name=_("Booking Date"),
    )
    category = models.ForeignKey(
        to="data.Category",
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        verbose_name=_("Category"),
    )
    bank_account = models.ForeignKey(
        to="data.BankAccount",
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        verbose_name=_("Bank Account"),
    )
    cash_flow_type = models.TextField(
        choices=CashFlowChoices.choices,
        null=False,
        default=CashFlowChoices.SPENDING,
        verbose_name=_("Cash Flow type"),
    )
    tax_consultant_relevant = models.BooleanField(
        default=False,
        null=False,
        blank=True,
        verbose_name=_("Tax Consultant relevant"),
    )
    business_related = models.BooleanField(
        default=False,
        null=False,
        blank=True,
        verbose_name=_("Business related"),
    )

    class Meta:
        verbose_name = _("transaction")
        verbose_name_plural = _("transactions")
