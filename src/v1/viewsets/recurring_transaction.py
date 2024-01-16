from rest_framework.viewsets import ModelViewSet

from data.models import RecurringTransaction
from v1.serializers import RecurringTransactionSerializer


class RecurringTransactionViewSet(ModelViewSet):
    queryset = RecurringTransaction.objects.all()
    serializer_class = RecurringTransactionSerializer
