from rest_framework.serializers import ModelSerializer

from data.models import BankAccount


class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = BankAccount
        fields = (
            "pk",
            "name",
            "IBAN",
            "owner",
        )
