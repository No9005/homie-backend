from rest_framework.serializers import ModelSerializer

from data.models import RecurringTransaction


class RecurringTransactionSerializer(ModelSerializer):
    class Meta:
        model = RecurringTransaction
        fields = (
            "pk",
            "amount",
            "description",
            "user",
            "date",
            "category",
            "bank_account",
            "cash_flow_type",
            "tax_consultant",
            "business_related",
            "private",
            "day",
        )
