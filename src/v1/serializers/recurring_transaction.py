from rest_framework.serializers import ModelSerializer

from data.models import RecurringTransaction


class RecurringTransactionSerializer(ModelSerializer):
    class Meta:
        model = RecurringTransaction
        fields = "__all__"
