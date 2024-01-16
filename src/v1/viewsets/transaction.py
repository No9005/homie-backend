from rest_framework.viewsets import ModelViewSet

from data.models import Transaction
from v1.serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = (
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
    ordering_fields = (
        "pk",
        "date",
    )
    ordering = ("pk",)
