from rest_framework.serializers import ModelSerializer

from data.models import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
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
        )
