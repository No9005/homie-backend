from rest_framework.viewsets import ModelViewSet

from data.models import BankAccount
from v1.serializers import BankAccountSerializer


class BankAccountViewSet(ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
