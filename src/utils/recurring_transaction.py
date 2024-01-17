from __future__ import annotations

import calendar
from typing import TYPE_CHECKING

from django.apps import apps
from django.utils import timezone
from django_q.models import Schedule

if TYPE_CHECKING:
    from data.models import RecurringTransaction, Transaction


def handle(recurring_transaction_id: int):
    transaction_model: Transaction = apps.get_model("data", "Transaction")
    recurring_transaction_model: RecurringTransaction = apps.get_model(
        "data",
        "RecurringTransaction",
    )

    recurring_transaction: RecurringTransaction = recurring_transaction_model.object.get(
        recurring_transaction_id
    )

    transaction_model.objects.create(
        amount=recurring_transaction.amount,
        description=recurring_transaction.description,
        user=recurring_transaction.user,
        date=timezone.now(),
        category=recurring_transaction.category,
        bank_account=recurring_transaction.bank_account,
        cash_flow_type=recurring_transaction.cash_flow_type,
        tax_consultant=recurring_transaction.tax_consultant,
        business_related=recurring_transaction.business_related,
        private=recurring_transaction.private,
    )
    return


def register(recurring_transaction: RecurringTransaction):
    now = timezone.now()
    try:
        next_run = (
            recurring_transaction.date
            if now < recurring_transaction.date
            else now.replace(day=recurring_transaction.day, month=now.month + 1)
        )
    except ValueError:
        month_range = calendar.monthrange(now.year, now.month + 1)
        next_run = now.replace(day=month_range[1], month=now.month + 1)

    # Caution: args has to be a iterable, so dont forget the comma at the end.
    Schedule.objects.get_or_create(
        name="recurring_transaction",
        func="utils.recurring_transaction.handle",
        args=f"{str(recurring_transaction.pk)},",
        schedule_type=Schedule.MONTHLY,
        next_run=next_run,
    )
    return


def unregister(recurring_transaction: RecurringTransaction):
    Schedule.objects.filter(args=f"{str(recurring_transaction.id)},").delete()
    return
