from rest_framework.viewsets import ModelViewSet

from data.models import Transaction
from v1.serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
